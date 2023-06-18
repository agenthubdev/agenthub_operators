# GmailReader Operator Documentation

## Summary

GmailReader is an operator that fetches unread emails from a Gmail account, uploads any attachments to Google Cloud Storage, and then provides the email data and attachment names as outputs.

## Inputs

- `email_id`: (Optional) The UID of a specific email to be fetched. If not provided, the operator fetches all unread emails.

## Parameters

- `email`: The email address of the Gmail account to fetch emails from.
- `password`: The password for the Gmail account.
- `mark_as_read`: (Optional) If set to 'True', the fetched emails will be marked as read. Default is 'False'.

## Outputs

- `email_data`: An array of email information, containing the email 'id' (UID), 'From', 'Subject', 'Date', 'Body', and 'Attachments'.
- `attached_file_names`: The list of attachment file names uploaded to Google Cloud Storage.

## Functionality

The `run_step` function of the operator takes the inputs and parameters, reads the emails using the `read_emails` function, and then sets the outputs with the fetched email data and attachment file names.

The `read_emails` function fetches the unread emails using the IMAP4_SSL protocol and decodes the email content into a readable format. It also handles uploading attachments to Google Cloud Storage using the `upload_attachments` function.

The `upload_attachments` function takes in the file paths of the attachments saved in a temporary directory and uploads them to Google Cloud Storage. The function returns a list of uploaded attachment file names.