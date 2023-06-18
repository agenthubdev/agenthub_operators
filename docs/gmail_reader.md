# **GmailReader**

The `GmailReader` class is a custom operator that retrieves unread emails from a Gmail account. It uses the IMAP protocol to connect to the inbox, and can retrieve the entire contents of the email including attachments. Optionally, it can mark the email as read after retrieval.

## Input
- `email_id` (optional): The unique ID of the email to retrieve. If not provided, retrieves all unread messages.

## Parameters
- `email`: The email address to connect to.
- `password`: The password for the email account.
- `mark_as_read`: Whether to mark the email retrieved as read (default is False).

## Outputs
- `email_data`: A list of JSON strings representing each retrieved email.
- `attached_file_names`: A list of the file names of any attachments that were uploaded to a specified destination.

## Helper methods
- `declare_name()`: Returns the name of the operator.
- `declare_category()`: Returns the category of the operator.
- `declare_parameters()`: Returns a list of dictionaries, where each dictionary contains metadata about an input parameter.
- `declare_inputs()`: Returns a list of dictionaries, where each dictionary contains metadata about an input.
- `declare_outputs()`: Returns a list of dictionaries, where each dictionary contains metadata about an output.
- `run_step(self, step, ai_context)`: Runs the operator and sets the output using the `ai_context` object provided.
- `read_emails(self, user, password, mark_as_read, email_id, ai_context)`: Reads emails from the Gmail account based on the input parameters, and returns a tuple of email data and uploaded files.
- `upload_attachments(self, file_paths, ai_context)`: Uploads attachments to a specified destination using the `ai_context` object provided.