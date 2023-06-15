## CastType

**CastType** is a class that extends _BaseOperator_, and its purpose is to convert data between different types, given the desired output type. The class contains several predefined input fields, parameters, and output fields which help to provide a schema for the casting operation.

### Inputs, Parameters, and Outputs

- Inputs:
    - `input`: a data of any type
- Parameters:
    - `output_type`: an enumeration value representing the desired output data type (string, string[])
- Outputs:
    - `output`: a data of any type, after the conversion

### Key Methods

1. `run_step()`: This method is responsible for determining the input and output types and performing the appropriate casting between the types, based on the provided parameters. The code contains different branches for handling different input-output type combinations:

   - If the input type is `Document[]` and the output type is `string`, the method joins the `page_content` attribute of each document in the input list.
   - If the input type is `string` and the output type is `[]` or `string[]`, the method calls the `best_effort_string_to_list()` helper function to convert the input string into a list.

   If the given input and output types can't be cast, a `TypeError` will be raised.

2. `best_effort_string_to_list()`: This method attempts to convert a given string to a list. First, it tries to parse the string as JSON, and if the parsed result is a dictionary, it wraps the dictionary in a list. If the parsed result is a list, the result is returned as is. If the string can't be parsed as JSON, the method tries to split the string by commas and returns a list of stripped items.