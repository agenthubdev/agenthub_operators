# BaseOperator

The **BaseOperator** class serves as a base or foundation for creating custom operator classes that can be used in processing pipelines. The main purpose of this class is to provide a consistent structure and set of methods for operators to inherit and customize based on their specific functionality.

This base class includes:

- A unique identifier (ID) for each operator instance, using the **shortuuid** library
- An **Enum** for categorizing operators into different categories
- A set of static methods for declaring operator properties, such as name, parameters, inputs, outputs, secrets, description, and category
- A `run_step` method, which serves as a placeholder for derived operator classes to implement their processing logic

## Important Sections

- **OperatorCategory Enum**: Provides categories that operators can be classified into. They include:
  - CONSUME_DATA: Data Intake
  - MANIPULATE_DATA: Data Manipulation
  - AI: Using Large Language Models
  - ACT: Interact with the World
  - MISC: The rest
- **declare_allow_batch**: Determines whether the AgentHub platform is allowed to execute the operator multiple times in a loop on vector inputs.
- **declare_name**: Returns the operator's user-visible name for use in the frontend.
- **declare_parameters**: Lists the operator's parameters, which users need to set manually when building a pipeline.
- **declare_inputs**: Specifies the input state that an operator processes, such as a list of web links or a blob of text.
- **declare_outputs**: Specifies the outputs that the operator produces, which can serve as inputs to other operators in a pipeline.
- **declare_secrets**: Lists the names of secrets that an operator may use.
- **declare_description**: Returns a plain English description of what the operator does (optional).
- **declare_category**: Specifies the category for the operator.

## Inputs, Parameters, and Outputs

- **Inputs**: The input state that an operator processes. These inputs cannot be set manually on the UI by users (currently), but can be taken from the outputs of previous operators in a pipeline.
- **Parameters**: Values that users need to set manually when building a pipeline, allowing for customization and configuration of the operator's behavior.
- **Outputs**: Specifies the output produced by the operator, which can serve as inputs for other operators in a pipeline.

By providing these methods and structure, the **BaseOperator** class makes it easier for developers to create and maintain a consistent set of operators for use in processing pipelines on the AgentHub platform.