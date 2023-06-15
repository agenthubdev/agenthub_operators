# AskChatGpt

The **AskChatGpt** class is a subclass of the *BaseOperator* class and is used to interact with ChatGPT by processing user questions and return relevant responses. The class contains several static methods and a single run_step method to achieve this functionality.

## Main Functionality:

- **declare_name()**: Returns the name of the operator as 'Ask ChatGPT'.
- **declare_category()**: Returns the category of the operator as BaseOperator.OperatorCategory.AI.value.
- **declare_allow_batch()**: Specifies whether the operator supports batch operations (True).
- **declare_parameters()**: Specifies the required parameters for the operator (question, context, and max_tokens).
- **declare_inputs()**: Specifies the input for the operator, which is context (optional).
- **declare_outputs()**: Specifies the output for the operator, which is chatgpt_response (string data type).
- **run_step(step, ai_context)**: The main function that processes the inputs, runs the AI context, and sets the output. This function combines the input context and parameter context if present, constructs the prompt to get the chat completion, and logs the response from ChatGPT.

### Inputs:

- *context*: Optional string data type input.

### Parameters:

- *question*: String data type.
- *context*: String data type, optional.
- *max_tokens*: Integer data type.

### Outputs:

- *chatgpt_response*: String data type.

By providing the necessary inputs and parameters, the **AskChatGpt** class generates relevant responses from ChatGPT and sets the output as `chatgpt_response`.