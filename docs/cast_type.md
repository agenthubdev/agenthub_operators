# Documentation

## Summary

The CastType operator is used for casting the input data to a specific output type, providing functionality to manipulate different data types within the AI context.

## Inputs

- **input**: The input parameter is a data of any type that will be subject to type casting based on the defined output type.

## Parameters

- **output_type**: The output_type parameter is an enumeration of possible types (string, string[]) to which the input data will be cast.

## Outputs

- **output**: The output parameter is the result of casting the input data to the specified output_type. The output datatype will be of the specified output_type.

## Functionality

The CastType operator provides functionality to cast input data into a specific output type. It handles various input types (Document[], string) and output types (string, [] or string[]).

### run_step

The run_step function first retrieves the input and input_type from the ai_context, as well as the output_type specified by the user/step. Depending on the input and output types, it may perform the following:

- For input_type "Document[]" and output_type "string", it will join the content of all documents in the input list into a single string.
- For input_type "string" and output_type "[]" or "string[]", it will convert the input string into a list best_effort_string_to_list function.

If there is no known way to cast the input_type to the desired output_type, it raises a TypeError.

### best_effort_string_to_list

The best_effort_string_to_list function attempts to convert the given string into a list. It first tries using json.loads(), and if successful, checks if the result is either a dictionary or a list. If the result is a dictionary, it will wrap the dictionary in a list. If json.loads() fails, the function will split the string by comma and return a list of stripped items.