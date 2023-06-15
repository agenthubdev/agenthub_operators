# StoreInDb

The **StoreInDb** class is a custom operator used for storing text data in a database. This operator is derived from the **BaseOperator** class and implements methods for declaring its name, category, input parameters, and outputs. 

## Main Functionality

The main functionality of this class is implemented by the `run_step` method, which takes two arguments: `step` and `ai_context`. The method reads the parameters from the step dictionary and then loads the input text. The text is firstly processed by either splitting it by lines or chunks, based on the `split_by` parameter. The word count of each chunk formed can be controlled using the `chunk_size_words` parameter. After processing, the chunks are stored in the database table by calling the `index_chunks` function with additional information like table name, visibility, language, and team name.

Some helper methods in this class are:

- `declare_name()`: Returns the name of the operator.
- `declare_category()`: Returns the category of the operator.
- `declare_parameters()`: Returns a list of dictionaries that define the operator's parameters along with their data types and optional placeholders.
- `declare_inputs()`: Returns a list of the input data types that the operator accepts.
- `declare_outputs()`: Returns an empty list as the operator has no output.

### Parameters

Some important parameters include table_name, visibility, split_by, chunk_size_words, and language:

- **table_name**: The database table in which the data will be stored.
- **visibility**: An enumeration of team, user, and public. Determines who can access the stored data.
- **split_by**: Determines how to split the input text (by line or chunk) before storing it.
- **chunk_size_words**: The desired word count for each chunk (applicable if split_by is set to chunk).
- **language**: An enumeration of supported languages for the data being stored.

### Input

- **text**: The input text that will be stored in the database

### Output

- The operator has no outputs.