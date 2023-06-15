## VectorizeOperator

The **VectorizeOperator** class is a subclass of `BaseOperator`, which aims to *manipulate data* by creating a list of a specified element repeated for a certain number of times.

### Key Methods

- `declare_name()`: Returns the name, **Vectorize**.
- `declare_category()`: Returns the category from `BaseOperator.OperatorCategory`. In this case, it is `MANIPULATE_DATA`.
- `declare_description()`: Provides a description of the functionality: **Creates a list out of 'element' of size len('vector') like so: [element] * len(vector).**
- `declare_parameters()`: Lists the parameters for this operator. No parameters are needed in this case.
- `declare_inputs()`: Lists the input data required. In this case, it requires *"element"* (any data type) and *"vector"* (any data type).
- `declare_outputs()`: Lists the output data produced. In this case, it produces *"vector_of_elements"* (any data type).
- `run_step()`: The main function that takes in the input data `element` and `vector`, creates a list with repeated *element* of length *vector*, and sets the output data as *"vector_of_elements"*.

### Usage

To use **VectorizeOperator**, provide an element and a vector. The function will create a list containing the given element repeated for a length equal to the length of the input vector. The output will be in the form of a list of the repeated element, under the name *"vector_of_elements"*.