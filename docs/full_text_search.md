# FullTextSearch

**FullTextSearch** is a class that inherits from `BaseOperator`. It scans input text in a sliding window fashion and returns windows that are most relevant to a given query. The results can be limited by the number of results and the window size, and an option to return results within a single line or multiline is also available. 

## Class Methods

### declare_* methods

These methods provide metadata about the class, including its name, description, allowed batch, category, inputs, outputs, and parameters.

### run_step

This method is the main function of the class. It performs a sliding window search using the given query, input text, and other parameters to find the most relevant windows.

It initializes the sliding window loop, expanding it based on the query tokens and tokens from the input text, and moves the beginning and end of the window until it reaches the end of the text. 

Relevance scores are calculated based on the token matches within the window, and the results are stored in a heap structure. Finally, the output is generated based on the most relevant windows found, and these results are added to the AI context.

## Helper Methods

These are some helper methods used within the class:

- `token_range_to_string`: Converts a token range to a string.
- `token_match_score`: Compares two tokens and returns a match score.
- `token_is_word`: Determines if the token is a valid word.

## Inputs, Parameters, and Outputs

- Inputs: `text` and `query` (optional)
- Parameters: `nresults`, `window_size`, `query`, and `multiline`
- Outputs: `search_result` and `search_results_metadata`