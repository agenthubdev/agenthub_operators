import email
import imaplib
import base64
import os
import tempfile
from google.cloud import storage

from .base_operator import BaseOperator
from ai_context import AiContext

class GmailReader(BaseOperator):
    @staticmethod
    def declare_name():
        return 'GmailReader'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.CONSUME_DATA.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "email",
                "data_type": "string",
                "placeholder": "Enter the email address",
            },
            {
                "name": "password",
                "data_type": "string",
                "placeholder": "Enter the password",
            },
            {
                "name": "mark_as_read",
                "data_type": "boolean",
                "placeholder": "Mark email as read (default is False)",
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "email_id",
                "data_type": "string",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "email_data",
                "data_type": "string[]", 
            },
            {
                "name": "attached_file_names",
                "data_type": "string[]",
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        params = step['parameters']
        email = params.get('email')
        password = params.get('password')
        mark_as_read_str = params.get('mark_as_read')
        email_id = ai_context.get_input('email_id', self)

        mark_as_read = False  # Default to False
        if mark_as_read_str and mark_as_read_str.lower() == 'true':
            mark_as_read = True
        
        email_data, uploaded_file_names = self.read_emails(email, password, mark_as_read, email_id, ai_context)
        ai_context.set_output('email_data', email_data, self)
        ai_context.set_output('attached_file_names', uploaded_file_names, self)        

    def read_emails(self, user: str, password: str, mark_as_read: bool, email_id: str, ai_context):
        all_email_data = []
        all_uploaded_files = []
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(user, password)
            mail.select("inbox")  # connect to inbox.

            if email_id:
                result, data = mail.uid('fetch', email_id, '(UID BODY.PEEK[])')  # Retrieve the specific email using its UID
            else:
                result, data = mail.uid('search', None, "(UNSEEN)")
            if result == 'OK':
                for num in data[0].split():  # iterate over all unread messages
                    result, data = mail.uid('fetch', num, '(UID BODY.PEEK[])')  # Retrieve UID along with email
                    if result == 'OK':
                        raw_email = data[0][1]
                        email_message = email.message_from_bytes(raw_email)
                        uid = data[0][0].decode().split()[2]  # Parse UID from response
                        body = ''
                        file_paths_to_save = []

                        with tempfile.TemporaryDirectory() as tempdir:
                            for part in email_message.walk():
                                if part.get_content_disposition() == 'attachment':
                                    file_data = part.get_payload(decode=True)
                                    file_name = part.get_filename()
                                    if file_name:
                                        file_path = os.path.join(tempdir, file_name)
                                        with open(file_path, 'wb') as temp:
                                            temp.write(file_data)
                                        file_paths_to_save.append(file_path)

                                elif part.get_content_type() == 'text/plain':
                                    text = part.get_payload(decode=True)
                                    charset = part.get_content_charset()
                                    if charset:
                                        text = text.decode(charset)
                                    body += text

                            # Upload attachments to Google Cloud Storage
                            uploaded_files = self.upload_attachments(file_paths_to_save, ai_context)

                        email_info = {
                            'id': uid,  # Use 'UID' as 'id'
                            'content': {
                                'From': email_message['From'],
                                'Subject': email_message['Subject'],
                                'Date': email_message['Date'],
                                'Body': body,
                                'Attachments': uploaded_files
                            }
                        }

                        all_email_data.append(str(email_info))
                        ai_context.add_to_log(f"Email {uid} with subject {email_info['content']['Subject']} has been read.")
                        if mark_as_read:
                            mail.uid('store', num, '+FLAGS', '\Seen')
                        
                        # TODO: switch to multi attachment support when looping functionality is added to operators
                        all_uploaded_files.append(uploaded_files[0] if uploaded_files else "")  # Add all uploaded files

                    else:
                        ai_context.add_to_log("No new email.")
            else:
                ai_context.add_to_log("No new email.")

            mail.logout()
            return all_email_data, all_uploaded_files

        except Exception as error:
            ai_context.add_to_log(f"An error occurred: {str(error)}")
            return [], []  # Return empty lists in case of error
        
    def upload_attachments(self, file_paths, ai_context):
        uploaded_files = []

        for file_path in file_paths:
            file_name = os.path.basename(file_path)

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    stored_file_name = ai_context.store_file(file, file_name)
                    if stored_file_name:
                        uploaded_files.append(stored_file_name)

        return uploaded_files
