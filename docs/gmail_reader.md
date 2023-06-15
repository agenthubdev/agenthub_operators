# GmailReader

The **GmailReader** class is a custom operator that reads emails from user's Gmail inbox. Given the user's email address and password, it fetches unread emails (or a specific email by ID) and returns the email data and attached file names as output.

## Parameters:

- `email`: Email address of the user
- `password`: Password of the user's email account
- `mark_as_read`: Whether to mark the fetched emails as read. Default is False.

## Inputs:

- `email_id`: (Optional) The ID of a specific email to read

## Outputs:

- `email_data`: Array of email content (From, Subject, Date, Body, and Attachments)
- `attached_file_names`: Array of filenames of attachments in the emails

### Main function: `run_step`

The `run_step` method takes input parameters, email ID (optional), and an AI context object and fetches emails from the user's Gmail inbox. It calls the `read_emails` method with the provided parameters.

### Helper methods

#### `read_emails`

This method logs into the user's Gmail account, selects the inbox, and fetches unread emails or a specific email by its ID. It handles the email retrieval, processing, and attachment uploading (if any) with the help of Google Cloud Storage.

#### `upload_attachments`

This method uploads the attachments of each email to Google Cloud Storage, storing the file under the run ID of the AI context. It returns a list of the uploaded file names.

Overall, the **GmailReader** class provides an easy way to read and process emails directly from a Gmail inbox.