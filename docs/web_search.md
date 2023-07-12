## Summary

This operator enables users to perform a Google web search and returns the top results.

## Inputs

- None

## Parameters

- `query`: A string that represents the user's search query.
- `results_count`: An integer that represents the number of desired search results.

## Outputs

- `urls`: A list of of the URLs from the web search
- `snippets`: These are "snippets" corresponding to each URL. Each snippet is a description of the website, similar to the preview you get through a Google Search.

## Functionality

### run_step()

This function is the main driver of the WebSearch operator. It generates a prompt based on the input query or the query parameter, then gets the AI's response and performs the required web search using the `google_search()` function. Finally, it processes the search results by extracting the URLs and snippets from them and sets the output of the operator with the search_results data.

### gen_prompt()

This function generates a prompt for the AI based on the given query parameter or input.

### google_search()

This function performs a Google web search using the given query and returns the specified number of results. It uses Google's Custom Search API and requires the developer's API key as well as a custom search engine ID for making the search request.

In case of an invalid API key or any other HTTP-related error, the function returns an error message accordingly.

### get_urls_and_snippets()

This function processes the raw search results data by extracting the URLs and snippets for each result. It returns two separate lists containing the extracted data.
