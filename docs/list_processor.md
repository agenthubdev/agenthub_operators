# ListProcessor

The **ListProcessor** class is a custom operator that extends the `BaseOperator` class. It is designed to process a list of elements by feeding the content of each element to an AI model and generating a new list containing the processed content. The main use case of this class is automating the processing of structured data with AI while keeping track of element names.

## Class Methods

- **declare_name():** Returns the string 'List Processor' as the identifier for this operator.
- **declare_category():** Returns the `BaseOperator.OperatorCategory.AI.value`, indicating this operator belongs to the AI category.
- **declare_parameters():** Defines a single parameter called `prompt` with data type `string`. This is the instruction given to the AI to perform a specific task with the list. For example, "Summarize the contents."
- **declare_inputs():** Declares a single input called `list` with data type `{name,content}[]`. This is an array of dictionaries containing two fields: `name` (a string) and `content` (the data to be processed).
- **declare_outputs():** Declares a single output called `result_list` with data type `{name,content}[]`. This is an array of dictionaries with the same structure as the input, but the content field contains the AI-processed data.

## run_step() Method

The `run_step()` method is the main method responsible for executing the processing logic. It takes two arguments: the `step` containing the operator's parameters, and an instance of `AiContext`, the context in which the AI model runs.

1. The method first checks whether the input list `'list'` is available. If not, it adds an error message to the log and returns `False`.
2. It initializes an empty `result_list` to store the processed content.
3. For each element `e` in the input list `l`:
   - Extract its content into the variable `content`.
   - Create a prompt by appending the content and the instruction from the `prompt` parameter.
   - Run the AI chat completion using the generated prompt and save the response in the variable `ai_response`.
   - Add the AI response to the logs.
   - Append a new dictionary with the same name and the new content (the AI response) to the `result_list`.
4. Set the output `'result_list'` to the generated `result_list`.
5. Return `True` to indicate successful execution.

In summary, the **ListProcessor** class allows you to process a structured list with an AI model based on a given instruction (prompt) and returns a new list with the processed content. The class makes use of several static methods to set the name, category, parameters, inputs, and outputs. The `run_step()` method manages the main processing logic by iterating over the input list, running the AI model on the content, and storing the results in a new list.