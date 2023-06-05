# GmailSender

The `GmailSender` class is a part of the AgentHub framework and it mainly focuses on sending emails using a Gmail account. This class extends the `BaseOperator` class and deals with the Gmail SMTP API to provide functionality for sending emails with or without HTML content. 

## Functionality

This class contains a set of predefined methods that help in defining various aspects of the operator, such as its parameters, inputs, and outputs. These aspects include:

### Parameters:

- **recipient_email**: A string that represents the email address of the recipient.
- **send_as_html**: A boolean that, when set to `True`, sends the email as HTML instead of plain text. Its default value is `False`.

### Inputs:

- **email_body**: A string containing the content of the email body.

### Outputs:

- **email_status**: A string indicating the status of the email sent. It can be either "Email sent successfully" or "Email sending failed".

## Main Functionality

The main functionality of the `GmailSender` class lies in its `run_step` method, which takes in a step configuration, an AI context, and reads the parameter values, such as the recipient's email and whether to send the email as HTML or plain text.

It then calls the `send_email` method that handles the actual email sending process. This method takes the following parameters:

- **subject**: The subject of the email.
- **body**: The content of the email body.
- **sender**: The sender's email address.
- **recipients**: A list containing the recipient email addresses.
- **password**: The sender's Gmail account password.
- **send_as_html**: A boolean indicating whether to send the email as HTML or plain text.
- **ai_context**: The AI context object where logs can be added.

The `send_email` method first creates an instance of the email message (either as an HTML or plain text message), and then establishes a connection to the Gmail SMTP server using the `smtplib.SMTP_SSL` class. It logs in to the sender's Gmail account using the provided email address and password, and then sends the email to the specified recipients. Finally, it logs out from the SMTP server and returns the status of the email sent (either successful or failed).

In case of any errors, the method logs the error message in the AI context, and returns an "Email sending failed" status.