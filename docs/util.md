# Code Documentation

This documentation explains the code provided in a structured format, with an emphasis on the helper functions and their functionality.

## **get_max_tokens_for_model**

This function receives a `model_name` as input and returns the maximum number of tokens supported by that model.

**Parameters:**
- `model_name` (str): The name of the model.

**Returns:**
- `max_tokens` (int): The maximum number of tokens supported by the given model.

## **cosine_distance**

This function calculates the cosine distance between two input vectors `v1` and `v2`.

**Parameters:**
- `v1` (array-like): The first input vector.
- `v2` (array-like): The second input vector.

**Returns:**
- `distance` (float): The cosine distance between the two input vectors.

## **count_tokens**

This function counts the number of tokens in the input string `s` using the encoding specified by the `model_name`.

**Parameters:**
- `s` (str): The input string to count tokens in.
- `model_name` (str): The name of the model to use for encoding.

**Returns:**
- `num_tokens` (int): The number of tokens in the input string.

## **sort_chunks_by_similarity**

This function sorts a list of text chunks by their similarity to a given query embedding.

**Parameters:**
- `query_emb` (array-like): The query embedding to compare text chunks against.
- `vector_index` (dict): A dictionary that maps embedding tuples to text chunks.

**Returns:**
- `chunks` (list): A sorted list of tuples containing the negative similarity, embedding tuple, and corresponding text chunk.

## **select_most_relevant_chunks**

This function selects the most relevant text chunks based on the sorted chunks, a token budget, and a given model name.

**Parameters:**
- `sorted_chunks` (list): A sorted list of tuples containing the negative similarity, embedding tuple, and corresponding text chunk.
- `token_budget` (int): The maximum number of tokens allowed for the output.
- `model_name` (str): The name of the model to use for encoding.

**Returns:**
- `selected_chunks` (list): A list of the most relevant text chunks within the token budget.