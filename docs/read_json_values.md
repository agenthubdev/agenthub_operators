# ReadJsonValues Operator Documentation

## Summary
The ReadJsonValues operator is designed to extract specific values from a given JSON string, providing a mechanism to access and manipulate nested or sequential JSON data.

## Inputs
- `json_string`: A string representation of the JSON object. This is the JSON data from which specific values will be extracted.

## Parameters
- `keys`: A comma-separated string representing the keys to be extracted from the JSON object. Nested keys should be separated by a period (e.g., `"key1,key2,key3"` for non-nested keys, and `"key1.subkey1,key2.subkey2"` for nested keys).

## Outputs
- `json_values`: A concatenated string displaying the extracted key-value pairs from the JSON object in the format: `key: value`.

## Functionality
The main function within this operator is `run_step`, which is responsible for receiving the JSON string and extracting the specified key values. It uses a helper function called `get_nested_values` to perform the actual extraction and concatenation of keys to their corresponding values. If an error occurs during the processing, a failure message is logged, and the operator terminates unsuccessfully. If the key values are extracted successfully, the concatenated string is returned, and the operator finishes its execution successfully.