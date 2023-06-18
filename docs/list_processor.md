# ListProcessor Operator Documentation

## Summary
The ListProcessor Operator processes items in a list, utilizing AI and following a given prompt, to produce a transformed list.

## Inputs
- **list**: An array of elements with a "name" and "content" field. This is the input list to be processed.

## Parameters
- **prompt**: A string that describes the AI's task or goal for processing the content of each list element.

## Outputs
- **result_list**: A transformed list with the same structure as the input, but containing AI-processed content based on the given prompt.

## Functionality

### run_step
The main function in this operator, `run_step`, processes each element in the input list by running the AI chat completion with a given prompt. It sets the transformed list as output within the AI context.

#### Helper functions
- `declare_name`: Returns the name of the operator as `List Processor`.
- `declare_category`: Returns the category of the operator as AI.
- `declare_parameters`: Returns a list of parameter specifications, such as the name and data type.
- `declare_inputs`: Returns a list of input specifications, such as the name and data type.
- `declare_outputs`: Returns a list of output specifications, such as the name and data type.