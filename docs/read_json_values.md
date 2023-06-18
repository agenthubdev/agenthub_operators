# ReadJsonValues

The **ReadJsonValues** class is a sub-class of the **BaseOperator** class that is responsible for extracting values from a given JSON string based on the specified keys. The *declare* methods declare the attributes of the operator such as its name, category, parameters, inputs, and outputs. 

The `get_nested_values` method is a helper method that recursively traverses the JSON object to extract the values of the specified keys. If a key contains a dot (.), it is split and the method is called recursively on the object corresponding to the first part of the key. If the value of the key is a list, the method is called on each item in the list.

The *run_step* method of the **ReadJsonValues** class takes a JSON string as input and the keys of the values to be extracted as a parameter. It uses the `json.loads` method to parse the JSON string into a Python object. It then calls the `get_nested_values` method to extract the desired values based on the specified keys. The extracted values are then joined into a string and added to the AI context log and set as output for further use.

## Inputs

- `json_string`: A JSON string that contains the values to be extracted.

## Parameters

- `keys`: A comma-separated list of keys specifying the values to be extracted.

## Outputs

- `json_values`: A string containing the extracted values of the specified keys.

Overall, the purpose of the **ReadJsonValues** class is to provide a simple way of extracting values from a JSON string based on the specified keys. It achieves this by recursively traversing the JSON object and extracting the values of the specified keys.