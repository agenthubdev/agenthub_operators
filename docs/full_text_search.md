# Full Text Search Operator

## Summary
This operator performs a full text search on the input text and returns the most relevant windows based on the given query.

## Inputs
- `text`: The input text to be searched. DataType: string.
- `query`: The query to search for in the text. DataType: string. Optional.

## Parameters
- `nresults`: Maximum number of search results. Default value: 5. DataType: integer.
- `window_size`: Search window size in words. Default value: 20. DataType: integer.
- `query`: The query to search for in the text. DataType: string.
- `multiline`: Determines whether to allow windows to span multiple lines. DataType: boolean.

## Outputs
- `search_result`: The search result, containing text snippets that are most relevant to the query. DataType: string.
- `search_results_metadata`: Metadata about the search results. DataType: {}[].

## Functionality
The main function, `run_step`, is responsible for performing the full text search. It takes in the input parameters and text and uses the `nlp` object from the imported `spaCy` library. This function does a sliding window search on the input text and calculates a relevance score for each window based on the frequency and score of matching query tokens in the window. The sliding window search takes into account the optional parameter `multiline`, which controls whether the search results can span multiple lines or not. The final search result is a combination of the most relevant windows, specified by the `nresults` parameter.

Below are the helper functions used within the `run_step` function:
- `token_range_to_string`: Given a window of tokens and the text, it converts the token range into a string.
- `token_match_score`: Given two tokens, this function calculates the score for a token match. It currently returns 1 if both tokens are the same, and 0 if they are different.
- `token_is_word`: Given a token, this function checks if it is a word token or not, by checking if it's not a punctuation, space, or stop word.