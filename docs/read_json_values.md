# ReadJsonValues

This class is designed to extract values from a JSON object based on provided keys. It extends the **BaseOperator** and is a part of the **MANIPULATE_DATA** category.

## Functionality

The main functionality of this class is provided in the `run_step()` method. It takes a JSON string as input, converts it to a JSON object, and then calls the `get_nested_values()` helper method to obtain the values associated with the provided keys. Finally, the output is set to a comma-separated string of these JSON values.

### Inputs

- **json_string**: A JSON string that needs to be converted into a JSON object.

### Parameters

- **keys**: A comma-separated string containing the keys for which values need to be extracted from the JSON object.

### Outputs

- **json_values**: A comma-separated string containing the extracted JSON values.

## Helper Methods

### `get_nested_values()`

This method is used to obtain the values associated with the provided keys in a JSON object. It takes two arguments, `json_object` and `keys`. The method is recursive and can handle nested keys that are separated by a dot ('.'). It returns a list containing the extracted values in a "key: value" format.

In summary, the **ReadJsonValues** class provides a simple way to extract values from a JSON object based on specified keys.