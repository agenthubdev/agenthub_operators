# CombineStrings Operator Documentation

## Summary
The `CombineStrings` operator combines two input strings as per the given format string.

## Inputs
- `input1`: (Optional) A string that serves as the first input string for combining.
- `input2`: (Optional) A string that serves as the second input string for combining.

## Parameters
- `format`: A string that specifies the format for combining the two input strings (for example, "This is input 1: {input1} This is input 2: {input2}").

## Outputs
- `combined_string`: The resulting combined string, created according to the provided format.

## Functionality
The `run_step` function takes the context object `AiContext`, extracts the necessary inputs and parameters for the operator, and combines the input strings using the provided format string. If the combination is successful, it logs the success message and sets the output with the resulting combined string. If an exception occurs, it logs the error message.