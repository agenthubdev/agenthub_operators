# ReadJsonValues

**ReadJsonValues** is a class that extends `BaseOperator` and is used to read the values of specified keys from a given JSON string and return them as a comma-separated string. The class has a helper method `get_nested_values` that recursively traverses the JSON object to extract the values of the specified keys.

### Inputs

- `json_string`: A string containing the JSON object that needs to be processed.
    - data_type: "string"
    - placeholder: "Enter the JSON string"

### Parameters

- `keys`: A comma-separated string of keys whose values need to be extracted from the JSON string.
    - data_type: "string"
    - placeholder: "Ex: 'key1,key2,key3'"

### Outputs

- `json_values`: A comma-separated string containing values of the specified keys stored in the input JSON string.
    - data_type: "string"

### Helper Method: get_nested_values

This method takes a JSON object and a list of keys and returns a list of extracted values in the format `key: value`. This method is used to recursively traverse the JSON object and extract nested values if required.

- **Arguments**:
    - `json_object`: The JSON object that needs to be traversed.
    - `keys`: A list of keys whose values need to be extracted from the input JSON object.

- **Returns**: A list of extracted values in the format `key: value`.