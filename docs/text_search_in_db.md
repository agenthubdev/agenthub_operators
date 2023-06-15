# TextSearchInDb

The **TextSearchInDb** class is a `BaseOperator` which helps to perform a **text search in a database**. It searches for a specific text query within a database table and returns the search results as output. 

It has the following methods:

- `declare_name()`: Returns the name of the operator as 'Text search in DB'.
- `declare_category()`: Returns the category of the operator as 'DB'.
- `declare_parameters()`: Defines the parameters needed for the text search.
- `declare_inputs()`: Defines the inputs to the operator.
- `declare_outputs()`: Defines the outputs from the operator.
- `run_step()`: Executes the text search and produces the output.

## Parameters

- `query`: The text query to search for.
- `num_results`: The limit on the number of results to return (default is 10).
- `table_name`: The name of the table in the database to search in.
- `visibility`: The visibility of the data (can be 'team', 'user', or 'public').
- `team_name`: The name of the team in case the visibility is set to 'team'.
- `language`: The language of the text data.

## Inputs

- `query`: The text query to search for (optional, can be an input instead of a parameter).

## Outputs

- `search_results`: The results of the text search as a string.

The class uses the `query_chunk_index()` method of the `AiContext` to perform the text search in the database, and then sets the output and adds a log entry.

**Note**: The generated output is in an unrendered markdown format so it can be copied into a markdown generator.