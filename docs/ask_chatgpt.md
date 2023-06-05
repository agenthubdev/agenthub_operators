# AskChatGpt

The **AskChatGpt** class is a _BaseOperator_ class that enables interaction with the ChatGPT language model to ask questions within a given context and process reponses. It is designed to be flexible, allowing for the use of either a given input context or a specified parameter context during its execution.

## Table of functions and methods

- `declare_name()`: Declare the name of the operator
- `declare_category()`: Declare the category of the operator
- `declare_allow_batch()`: Declare batch processing
- `declare_parameters()`: Declare the input parameters
- `declare_inputs()`: Declare the input data structure
- `declare_outputs()`: Declare the output data structure
- `run_step(step, ai_context)`: Main method to run the ChatGPT language model and store the response

## Parameters

- `question`: A string representing the question to be asked of ChatGPT
- `context`: An optional string representing the context for the language model to use when answering the question
- `max_tokens`: An integer indicating the maximum number of tokens in the response

## Inputs

- `context`: An optional string representing input context. It is marked as optional since it can be provided directly as an input or as a parameter.

## Outputs

- `chatgpt_response`: A string representing the response received from ChatGPT after processing the question in the given context

## Helper methods

In addition to the main `run_step` method, the class has several helper methods that define its properties, such as allowing batch processing, declaring parameters, inputs, and outputs.

### declare_name

This static method returns the name of the operator: `'Ask ChatGPT'`

### declare_category

This static method returns the category of the operator as `BaseOperator.OperatorCategory.AI.value`

### declare_allow_batch

This static method returns a boolean value representing whether the operator allows batch processing: `True`

### declare_parameters

This static method defines the input parameters for the **AskChatGpt** class as a list of dictionaries describing their name, data_type, and placeholder.

### declare_inputs

This static method defines the input data structure for the **AskChatGpt** class as a list of dictionaries describing their name, data_type, and optional flag.

### declare_outputs

This static method defines the output data structure for the **AskChatGpt** class as a list of dictionaries describing their name, and data_type.

## run_step

The `run_step` method is the main execution method for the **AskChatGpt** class. It takes two arguments: the `step` containing parameters and the `ai_context` that holds the state of the AI flow.

It first extracts the question, input context, and papameter context from the given parameters. Then, it concatenates the input and parameter contexts with appropriate formatting, if needed. Next, it generates the prompt for the language model based on the question and context. Afterward, it runs the ChatGPT language model with the generated prompt and receives a response. Finally, the method stores the received response as an output in the AI context and logs the response for further use.