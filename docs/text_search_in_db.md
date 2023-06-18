# **TextSearchInDb**

This class is a sub-class of the `BaseOperator` class and it provides a text search functionality in a specified table of a database. It takes in a search query, the number of desired search results, the name of the table to search in, visibility level, team name (if visibility is set to "team"), and preferred language for search. 

The `run_step` method takes the given parameters and uses `ai_context.query_chunk_index()` method from `AiContext` class to search the database for the query. It then saves the search results to the `search_results` output.

This class has also implemented static helper methods to declare the name, category, parameters, inputs, and outputs.


## Inputs
The class takes in one optional input `query` which can also be given as a parameter.


## Parameters
1. `query`: query to search for in the database, it can also be passed as an input.
2. `num_results`: (optional) maximum number of search results to return, default is 10.
3. `table_name`: name of the table in the database to search in.
4. `visibility`: level of visibility of the table (team, public or user).
5. `team_name`: name of the team (if `visibility` is set to "team").
6. `language`: preferred language for search.


## Outputs
1. `search_results`: a string representation of the search results.


Overall, this class provides an easy way to search a database for a text query with the specified criteria.