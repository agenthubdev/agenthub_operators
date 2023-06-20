# Full Text Search Operator

## Summary
The Full Text Search operator scans text input in a sliding window fashion and returns up to 'nresults' windows that are most relevant to 'query' input/parameter.

## Inputs
* `text` (string): Input text for searching.
* `query` (string, optional): Query string used for search.

## Parameters
* `nresults` (integer, optional, default=5): Maximum number of search results to return.
* `window_size` (integer, optional, default=20): Search window size in words.
* `query` (string): Query string used for search.
* `multiline` (boolean, optional): Whether to allow windows span multiple lines.

## Outputs
* `search_result` (string): Output string containing the search results.
* `search_results_metadata` (list): Output list containing search results metadata.

## Functionality
The `run_step` function implements the Full Text Search algorithm using the following steps:
1. Get the input parameters and text.
2. Tokenize the text using the Spacy library.
3. Create a deque for each token in the query string and initialize the initial token positions to 0.
4. Traverse the tokenized text using a sliding window approach.
5. Calculate the relevance scores of the tokens in the query string that match the current sliding window.
6. Add the current sliding window with its relevance score to a heap.
7. Repeat steps 4-6 until the entire text has been scanned.
8. Retrieve the highest scoring sliding windows from the heap.
9. Merge overlapping sliding windows.
10. Output the search results and metadata.