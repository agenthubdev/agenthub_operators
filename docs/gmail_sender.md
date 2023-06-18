# Summary
The `GmailSender` operator sends an email using Gmail SMTP with the specified content.

# Inputs
- `email_body`: A string containing the email body to be sent.

# Parameters
- `recipient_email`: A string representing the recipient's email address.
- `send_as_html`: A boolean that decides whether to send the email as HTML (default is False).

# Outputs
- `email_status`: A string indicating the status of the email sending process, either "Email sent successfully" or "Email sending failed".

# Functionality
The `run_step` function is responsible for the main logic of the operator. It reads the recipient email and the send_as_html flag from the parameters, and the email body from the inputs. It also retrieves the Gmail sender and password from the AI context. It then calls the `send_email` helper function with the necessary parameters to send the email.

The `send_email` function configures the email message using MIMEText or MIMEMultipart based on whether the email is to be sent as HTML or not, logs in to the Gmail SMTP server and sends the email to the recipients. It returns the status of the email sending process as a string.