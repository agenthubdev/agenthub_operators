# **FullTextSearch**

This class provides functionality to scan input text in sliding window fashion and return the most relevant windows to a given query input, up to the specified maximum number of search results. The windows may be restricted to a single line if required. 

**Inputs:**
- text: string input text to be searched
- query (optional): string query to search for within the text

**Parameters:**
- nresults: maximum number of search results to return (default: 5)
- window_size: size of search window in words (default: 20)
- query: query to search for within the text
- multiline: whether to allow windows to span multiple lines (default: false)

**Outputs:**
- search_result: string of the most relevant search results
- search_result_metadata: metadata output that is not currently used.

### Helper Methods

- *token_range_to_string(window, text)*: takes a window range of tokens and the input text and returns a string representation of the window.
- *token_match_score(t1, t2)*: takes two tokens and matches them, returning a 1.0 if the tokens match
- *token_is_word(token)*: takes a token and returns True if it is not punctuation, space or a stopword.

### Method: *run_step*

Takes inputs, parameters and context and performs the required full text search on the input text. It uses several internal helper methods to tokenize the input text, match the query tokens to text tokens and calculate the relevance score of each window in the text. Once the sliding window search is complete, the top ranked windows (up to nresults) are selected and returned as the final output.