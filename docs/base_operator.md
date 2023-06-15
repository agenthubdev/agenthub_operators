# BaseOperator

The **BaseOperator** class is a foundational class for creating a variety of operators that can be used in a pipeline. These operators can be related to consuming data, manipulating data, database I/O, using LLMs, interacting with the world, and other miscellaneous tasks. Derived operator classes should properly set their names and other important information.

## Key Components

- **`declare_allow_batch()`**: Determines if the AgentHub platform should execute the operator multiple times in a loop on vector inputs.

- **`declare_name()`**: A user-visible operator name that users select on the frontend.

- **`declare_parameters()`**: Parameters that users need to set manually when building a pipeline.

- **`declare_additional_parameters()`**: Additional configuration options, like model preferences for operators that call LLMs.

- **`declare_inputs()`**: Input states that the operator processes, e.g., a list of web links or a blob of text.

- **`declare_outputs()`**: Outputs of the current operator which will be the inputs of the next operator in the pipeline.

- **`declare_secrets()`**: Names of secrets that the subject operator would use.

- **`declare_description()`**: A plain English explanation of what the operator does, optional.

- **`declare_category()`**: The category the operator falls into, which helps guide operator selection in the UI.

### Inputs, Parameters, and Outputs

- **Inputs**: States that the operator processes, like a list of web links or a text blob.

- **Parameters**: Values that users need to set manually when building pipelines, such as model preferences or API keys.

- **Outputs**: The results of the operator after processing inputs, which become inputs of the next operator in the pipeline.