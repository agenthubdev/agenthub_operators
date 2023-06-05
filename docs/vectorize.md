# VectorizeOperator

**VectorizeOperator** is a class that inherits from **BaseOperator**. Its main functionality is to create a list containing repeated 'element' values of a given length. This length is determined by the provided 'vector'. This operation can be useful when you need to fill a list with a specific value according to a certain size.

## Class Methods

### declare_name

Returns the operator's name: `'Vectorize'`.

### declare_category

Returns the operator's category: `BaseOperator.OperatorCategory.MANIPULATE_DATA.value`.

### declare_description

Provides a description of the functionality: 

```
"Creates a list out of 'element' of size len('vector') like so: [element] * len(vector)"
```

### declare_parameters

There are *no* parameters declared for this operator.

### declare_inputs

The operator requires two inputs:

1. `element`: This input can be of any data type and will be the value repeated in the resulting list.
2. `vector`: This input can also be of any data type, and its length determines the size of the resulting list.

### declare_outputs

The operator provides one output:

1. `vector_of_elements`: This output will be a list of the same length as 'vector', comprised of the repeated 'element' values.

## run_step

This method is responsible for the main functionality of the class. It creates the list containing the repeated 'element' values, based on the length of the 'vector' input. The result is then set as the output 'vector_of_elements'.