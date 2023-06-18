# BaseOperator Documentation

## Summary

BaseOperator is a base class for constructing pipeline operators, providing a generic structure and methods for managing inputs, outputs, parameters, and AI model preferences.

## Inputs

Inputs are the data that an operator processes, such as a list of web links or a blob of text. The `declare_inputs()` method is used to define these inputs.

## Parameters

Parameters are the user-defined settings for building a pipeline. They should not be confused with inputs. The `declare_parameters()` method is used to define them. Additionally, the `declare_additional_parameters()` method can be used to declare extra configurations for individual operator instances.

## Outputs

Outputs are the processed data or results produced by an operator. These outputs can serve as inputs for another operator. The `declare_outputs()` method is used to define these outputs.

## Functionality

### run_step

The `run_step()` method executes the operator's core functionality using the given AI context. This method should be implemented by the derived operator classes.

### Helper Functions

- `declare_allow_batch()`: Used to determine if the AgentHub platform can execute the operator multiple times in a loop on a vector of inputs.
- `declare_name()`: Provides a user-visible operator name for frontend display.
- `declare_secrets()`: Lists the names of secrets that the operator would use.
- `declare_description()`: Provides a plain English explanation of the operator.
- `declare_category()`: Specifies the category that the operator falls into, which helps guide the operator selection in the UI.

## OperatorCategory Enumeration

The `BaseOperator.OperatorCategory` enumeration class helps classify the different categories of operators. These categories include:

1. CONSUME_DATA (Data Intake)
2. MANIPULATE_DATA (Data Manipulation)
3. DB (Database I/O)
4. AI (Using LLMs)
5. ACT (Interact with the World)
6. MISC (The rest)