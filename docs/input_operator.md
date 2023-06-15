# InputOperator

The **InputOperator** is a special type of operator that serves two main purposes:

1. *Create a named input* for a pipeline
2. *Store the history of interactions* with the pipeline when it implements the action of an Agent

This operator is particularly useful when building interactive agents and for testing purposes. It allows you to manually specify the 'value' parameter for an Input operator.

Some key sections of the code include:

- The **declare_name()** method, which returns the name of this operator: `'Input'`
- The **declare_description()** method, which provides a brief description of the operator's functionality
- The **declare_category()** method, which returns the category of the operator: `BaseOperator.OperatorCategory.MISC.value`
- The **declare_parameters()**, **declare_inputs()**, and **declare_outputs()** methods, which define the required parameters, inputs, and outputs for the operator
- The **run_step()** method, which executes the operator's main functionality

The **InputOperator** has the following *parameters*:

- `value` (string): The string value you would like this operator instance to output
- `input_name` (string): Named input for the pipeline, can be used to invoke the pipeline with specified input values
- `store_log` (boolean): Whether you want to keep track of all the inputs that this pipeline was run with
- `log_visibility` (enum[user,team]): When storing the history of inputs for this saved pipeline, what level of granularity should the log be stored at (only available if `store_log` is true)
- `team_name` (string): Team name to store the logs for (only available if `log_visibility` is set to 'team')

The **InputOperator** has *no inputs* and one *output*:

- `output` (string): The outputted string value specified in the 'value' parameter

To use the InputOperator, simply create an instance of the operator and execute the `run_step()` method with the appropriate step and ai_context.