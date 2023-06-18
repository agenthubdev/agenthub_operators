# Vectorize Operator Documentation

## Summary

The Vectorize Operator creates a list of elements of the same size as the input vector.

## Inputs

- `element`: The element to be used to create the list. This can be of any data type.
- `vector`: The input vector to be used for determining the length of the resulting list. This can be of any data type.

## Parameters

- There are no parameters to be set for this operator.

## Outputs

- `vector_of_elements`: The resulting list containing the "element" repeated to match the length of the input vector. The output data type will be the same as the input "element".

## Functionality

The `run_step` method extracts the `element` and `vector` from the input, calculates the length of the vector, and creates a new list by repeating the `element` as many times as the length of the `vector`. Finally, it sets the output value as this new list. There are no additional helper functions in this operator.