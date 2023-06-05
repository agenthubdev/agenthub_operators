# SleepOperator

The **SleepOperator** is a simple class that extends from the `BaseOperator`. Its main purpose is mostly for testing and does nothing else other than making the program sleep for a given amount of time. This class doesn't have any input or output data, but has one parameter that needs to be provided.

## Description
`declare_description` returns the description of this operator as: `'Just sleeps and does nothing useful, we are mostly adding it for testing purposes.'`

## Name
`declare_name` returns the name of this operator as: `'Sleep Operator'`

## Category
`declare_category` returns the category of this operator, which is the `MISC` category.

## Parameters
`declare_parameters` returns a list of parameters required by this operator:

- `sleep_seconds`: A string representing the number of seconds that the program should sleep for. This value will be converted to float before being used.

## Inputs
`declare_inputs` returns an empty list, as this operator doesn't have any input data to work with.

## Outputs
`declare_outputs` returns an empty list, as this operator doesn't have any output data.

## Method: run_step
This method takes the step and the ai_context as its input arguments and uses the `sleep_seconds` parameter to make the program sleep for the specified amount of time. It doesn't have any output or specific functionality other than pausing the program execution for the given time.