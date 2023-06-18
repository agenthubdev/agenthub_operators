# OutputOperator Documentation

## Summary

The `OutputOperator` is a special operator used to (1) create a named output of a pipeline, and (2) store the output of saved pipelines (e.g., for interacting with an Agent in chat mode).

## Inputs

- `output`: A variable of any data type that is intended to be the output of the operator.

## Parameters

- `output_name`: A string parameter to give the pipeline output a name.
- `store_log`: A boolean parameter, which states if the output should be preserved when making this pipeline an Action of an Agent.
- `log_visibility`: An enum(user, team) parameter specifying the log's storage level of granularity when storing history of outputs for an Agent.
- `team_name`: A string parameter representing the team name to store the logs for (only applicable if `log_visibility` is set to "team").

## Outputs

There are no specific outputs for this operator, as it serves to store and name pipeline outputs.

## Functionality

- `declare_name()`: Static method that returns the operator name 'Output'.
- `declare_description()`: Static method that returns a description of the operator.
- `declare_category()`: Static method that returns the operator category as BaseOperator.OperatorCategory.MISC.value.
- `declare_parameters()`: Static method that declares the parameters of the operator.
- `declare_inputs()`: Static method that declares the inputs of the operator.
- `declare_outputs()`: Static method that declares the outputs of the operator (empty, as outputs are stored and managed through the provided parameters).
- `run_step(step, ai_context)`: A method that does nothing, the agenthub.dev platform implements special treatment for Input and Output operators. The OutputOperator is not performing any operation on the input data, and its main purpose is to store and manage outputs in the pipeline.