# InputOperator

The `InputOperator` is a special operator that serves two main purposes: 

1. It allows for the creation of a named input for a pipeline
2. It stores the history of interactions with the pipeline when it is used by an Agent.

This operator is particularly useful when building interactive agents, as the logging functionality allows for tracking user inputs and behaviors. 

## Important Methods

### `declare_name()`

This static method returns the name of the operator ('Input') as a string.

### `declare_description()`

This static method returns a description of the operator functionality and parameters as a string.

### `declare_category()`

This static method specifies the `OperatorCategory` used by the operator. In this case, it is the 'MISC' category.

### `declare_parameters()`

This static method returns a list of dictionaries describing the input parameters of the operator. These input parameters allow for customization of the operator instance, such as setting the 'value' parameter for manual testing or configuring logging options.

### `declare_inputs()`

This static method returns a list of dictionaries describing the input connections of the operator, which is an empty list for the `InputOperator`.

### `declare_outputs()`

This static method returns a list of dictionaries describing the output connections of the operator. In this case, it specifies the output as a string, with a key of 'output'.

### `run_step()`

This method is called when the operator is executed. It sets the 'output' parameter to the value specified in the 'value' input parameter.

## Inputs, Parameters, and Outputs

### Inputs

There are no input connections for the `InputOperator`.

### Parameters

- `value`: A string value that the operator instance will output
- `input_name`: A named input for the pipeline, to be used to invoke the pipeline with specified input values
- `store_log`: A boolean value indicating whether to save the history of inputs used with this pipeline - useful for interactive agents and logging user inputs
- `log_visibility`: An enum with values 'user' or 'team', indicating the level of granularity to store the saved pipeline history
- `team_name`: A string value indicating the team name to store the saved pipeline logs for

### Outputs

- `output`: A string value output by the operator instance