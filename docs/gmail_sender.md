# GmailSender

The **GmailSender** class allows users to send emails using the Gmail SMTP server. It is a subclass of `BaseOperator` and has a static method to declare its name, category, parameters, inputs, and outputs.

## Inputs, Parameters and Outputs

- **Inputs**:
    - `email_body`: A string representing the content of the email.

- **Parameters**:
    - `recipient_email`: A string, the email address of the recipient.
    - `send_as_html`: A boolean, indicating whether the email should be sent as HTML or not (default is False).

- **Outputs**:
    - `email_status`: A string, indicating whether the email was sent successfully or an error occurred.

## Functionality

#### declare_name, declare_category, declare_parameters, declare_inputs, declare_outputs

These static methods are used to declare the necessary information about the operator, such as its name, category, parameters, inputs, and outputs.

#### run_step

The `run_step` method is where the main functionality of the class resides. It first retrieves the necessary parameters, inputs, and secrets from `ai_context`. Then, it calls the `send_email` helper method to send the email and stores the result in the output `email_status`.

#### send_email

This helper method sends an email using the given subject, body, sender, recipients, password, and an optional flag to send the email as HTML. It connects to the Gmail SMTP server, logs in with the provided email and password, sends the email, and logs out. The method returns a status message indicating if the email was sent successfully or not.

In case of any exceptions, an error message is logged to `ai_context` and the method returns a failure status.