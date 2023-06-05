# FullTextSearch

The `FullTextSearch` class is a subclass of `BaseOperator`, which provides an implementation for performing full-text searches on a given input text with respect to a query. This class implements methods for declaring operator metadata, parameter information, and running the actual search step.

**Parameters:**
- **`nresults`** (integer): The maximum number of search results. Default is 5.
- **`window_size`** (integer): The search window size in words. Default is 20.
- **`query`** (string): The query to search for in the input text.
- **`multiline`** (boolean): Flag indicating whether to allow windows to span multiple lines or not.

**Inputs:**
- **`text`** (string): The input text on which the full-text search will be performed.
- **`query`** (string, optional): The input query for the search.

**Outputs:**
- **`search_result`** (string): The generated search result.
- **`search_results_metadata`** ({}[]): Metadata of the search results.

The class contains the following helper methods:

- *`token_range_to_string`*: Converts a range of tokens in the given text to a string representation.
- *`token_match_score`*: Computes the match score between two tokens.
- *`token_is_word`*: Determines if a given token is a word or not.

## Functionality

The `run_step` method is where the actual full-text search is performed. It starts by initializing necessary variables and retrieving input values. The search is performed in a sliding window fashion and returns up to `nresults` windows that are most relevant to the given query. The sliding window size is determined by the parameter `window_size`.

The search is performed using a multidimensional deque `qd`, where each deque stores the query tokens' matching entries in the input text `t`. The algorithm manages a window of tokens [be_i, en_i] in the input text, and calculates a total relevance score `total_s` for this window. The window is slid across the text until all windows have been examined, then relevant windows are merged if they overlap; this process is repeated up to `nresults` times to form the final search results, which are output as a string.