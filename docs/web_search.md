## WebSearch

**WebSearch** is a class that inherits from the BaseOperator class and provides functionality to search Google for a given query, leveraging Google's Custom Search API to retrieve specified number of search results including links and snippets. The main method this class provides is `run_step()`, which runs the search, retrieves the results, and sets the output to be consumed by further operators.

### Inputs:
- `query`: A string containing the search query.

### Parameters:
- `query`: A string containing the search query.
- `results_count`: An integer specifying the number of search results to be returned.

### Outputs:
- `search_results`: A list of dictionaries containing search results with the URL in the 'name' key and snippet in the 'content' key.

### Helper methods:

- `declare_name()`: A static method that returns the name of the operator as 'Web search'.
- `declare_category()`: A static method that returns the category of the operator set to BaseOperator.OperatorCategory.CONSUME_DATA.value.
- `declare_parameters()`: A static method that returns a list of dictionaries, providing information about the parameters that this operator expects.
- `declare_inputs()`: A static method that returns an empty list to signify that the operator does not accept any inputs.
- `declare_outputs()`: A static method that returns a list of dictionaries, providing information about the expected output of the operator.
- `get_urls_and_snippets(google_res)`: A method that takes the Google Search API response (as a dictionary) and extracts the URLs and snippets for each search result, returning them as separate lists.
- `gen_prompt(step, ai_context)`: A method that generates a prompt for the AI model based on the given query, so it can provide a suitable search query.
- `google_search(query, num_results, ai_context)`: A method that connects to Google's Custom Search API with the given query and specified number of results, returning a list of URLs as the search results.

### Usage:

The class is used to perform a Google search based on user input. It can be instantiated with particular inputs, parameters, and outputs specified by the user.

After running the `run_step()` method with the given `step` parameter and the AI context, it generates a search query using the AI model, sends the query to Google's Custom Search API, retrieves the search results, and finally sets the output containing the search results. These output results can be consumed by other operators in the processing pipeline.