# Input Operator

## Summary

This operator is a special type of operator used to create a named input for a pipeline and store history of interactions with the pipeline when it implements action of an Agent.

## Inputs

InputOperator has no inputs since this operator is used as a starting point of a pipeline to receive the initial input required for the pipeline to function.

## Parameters

The following parameters can be set for the InputOperator:

1. `value`: The string value you would like this operator instance to output.
2. `input_name`: Named input for the pipeline, can be used to invoke the pipeline with specified input values.
3. `store_log`: Specifies whether to keep track of all the inputs that this pipeline was run with. Useful when building interactive agents and less so for one-off experiments.
4. `log_visibility`: Determines the level of granularity that the log should be stored at when storing the history of inputs for this saved pipeline. The available options are `user` and `project`. It is only applicable when `store_log` is set to true.

## Outputs

The InputOperator emits the following output:

1. `output`: The string value passed to the `value` parameter during instantiation.

## Functionality

The core functionality of the InputOperator lies in its `run_step` function. This function takes in the `step` object and `ai_context` and sets the output of the operator using the `value` parameter. No additional helper functions are needed in this operator as the core functionality is relatively simple.
