# CombineStrings

**CombineStrings** is a class that inherits from the `BaseOperator`. Its main purpose is to concatenate two input strings according to a given format.

## Class Methods

- `declare_name()`: Returns the name of the operator, `'CombineStrings'`.
- `declare_category()`: Returns the category of the operator, which is _MANIPULATE_DATA_.
- `declare_parameters()`: Declares the parameters required for this operator. This operator accepts a single format parameter (a string) as input.
- `declare_allow_batch()`: Indicates whether this operator can handle batch processing. In this case, it returns `True`.
- `declare_inputs()`: Declares the inputs required for this operator. It accepts two strings, 'input1' and 'input2', which are both optional.
- `declare_outputs()`: Declares the output expected from this operator, which is a single 'combined_string' of data type string.

## Main Functionality

The `run_step()` method takes in a step and an AI context. It fetches the values of 'input1' and 'input2' from the AI context, and if not provided, defaults them to empty strings. It then fetches the format string from the step's parameters.

The method tries to substitute the input1 and input2 values into the format string by utilizing the `str.format()` method. If successful, it adds a log message and sets the combined_string as the output in the AI context. If it encounters any error during the process, a log message with the error information is added.