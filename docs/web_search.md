# **WebSearch**

This class represents an operator used for making Google searches and outputting the search results. It uses the Google Custom Search API and AI chat completion to take in a query (either from user input or a parameter) and return a list of URLs and snippets for the top results of a Google search. 

## Inputs
- None

## Parameters
- **query**: (string) The search query to be used for the Google search
- **results_count**: (integer) The number of search results to be returned

## Outputs
- **search_results**: A list of dictionaries containing the URL and snippet for each search result. 

## Helper Methods

### `declare_name()`
- Returns the name of the operator as a string.

### `declare_category()`
- Returns the category of the operator as a string (in this case, "CONSUME_DATA").

### `declare_parameters()`
- Returns a list of dictionaries containing the name, data type, and placeholder text for each parameter.

### `declare_inputs()`
- Returns a list of inputs for the operator (in this case, an empty list since there are no inputs).

### `declare_outputs()`
- Returns a list of outputs for the operator, which consists of a list of dictionaries containing the URL and snippet for each search result.

### `run_step(self, step, ai_context)`
- Gets the search query from either user input or a parameter.
- Uses the query to make a Google search and extract the URLs and snippets for the top results.
- Outputs the list of search results to the "search_results" output.

### `get_urls_and_snippets(self, google_res)`
- Extracts the URLs and snippets from the Google search results.
- Returns two lists: one containing the titles and snippets, and one containing the URLs.

### `gen_prompt(self, step, ai_context)`
- Generates a prompt for AI chat completion to get the search query from the user.
- Returns the prompt as a string.

### `google_search(self, query, num_results, ai_context) -> list[str]`
- Uses the Google Custom Search API to make a Google search.
- Returns the search results as a list of dictionaries.