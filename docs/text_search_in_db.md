# TextSearchInDb Operator Documentation

## Summary

TextSearchInDb operator performs a text search in a specified database table and returns search results with configurable parameters.

## Inputs

- `query`: the text string to search for, this can either be an input or a parameter. It is optional.

## Parameters

- `query`: the text string to search for, this can either be an input or a parameter if not provided as an input.
- `num_results`: limit on the number of results to return, it is optional and defaults to 10.
- `table_name`: name of the table to search in.
- `visibility`: specifies the visibility mode of the table as an enum(project, user, public).
- `language`: specifies the language to search in, provided as an enumeration of language options.

## Outputs

- `search_results`: a string of search results found in the database table.

## Functionality

The `run_step` function executes the primary operation of this operator. It first retrieves the query text string from the input or the provided parameters. Then, it calls the `query_chunk_index` helper function from the `AiContext` to perform the actual search operation while passing the additional parameters such as limit, table_name, visibility, and language.

Finally, it sets the output 'search_results' and logs the search results found.
