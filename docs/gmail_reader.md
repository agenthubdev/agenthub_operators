# GmailReader

**GmailReader** is a class that extends the **BaseOperator**. It's main purpose is to connect to a Gmail account, read emails (consuming data), and optionally upload attachments to Google Cloud Storage for further processing.

## Inputs
- **email_id** (string, optional): If provided, only the specific email with the given email_id will be retrieved. If not provided, unread emails in the inbox will be retrieved.

## Parameters
- **email** (string): The email address that the GmailReader will connect to.
- **password** (string): The password for the email account.
- **mark_as_read** (boolean): If set to true, the email(s) will be marked as read after being processed. If not provided or set to false, the emails will remain unread.

## Outputs
- **email_data** (string[]): A list containing the extracted email data that includes the following information for each email: id, From, Subject, Date, Body, and the uploaded file names (if any).
- **attached_file_names** (string[]): A list containing the attached files' names found in the emails.

## Helper Methods

### read_emails

`read_emails` is responsible for handling the main functionality of the GmailReader, connecting to the Gmail account, reading emails, uploading attachments to Google Cloud Storage, and extracting relevant data. It takes the following parameters:

- **user** (str): The email address.
- **password** (str): The password for the email account.
- **mark_as_read** (bool): Indicates if the emails should be marked as read after processing them.
- **email_id** (str): If provided, only the email with the given email_id will be retrieved. If not provided, unread emails in the inbox will be retrieved.
- **ai_context**: An object to access and manage the context of the AI run.

It returns two lists: `all_email_data` which contains the extracted email data, and `all_uploaded_files` which contains the file names of the uploaded attachments.

### upload_attachments

`upload_attachments` is a helper method to upload the attachments found in the emails to Google Cloud Storage, using the provided `file_paths` and `ai_context`. It takes the following parameters:

- **file_paths**: A list of file paths pointing to the attachments to be uploaded.
- **ai_context**: An object to access and manage the context of the AI run.

It returns a list `uploaded_files` containing the file names of the uploaded attachments.