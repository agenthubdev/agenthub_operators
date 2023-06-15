## TikToken and Text Analysis Functions

This code contains several functions and methods related to text analysis using tiktoken and calculating the cosine similarity for vector comparison. Below are the major components and a brief description of their functionality.

**1. `get_max_tokens_for_model(model_name: str) -> int`:**

This function accepts a model name as input and returns the maximum number of tokens allowed for that model. If the specified model is not supported, an error will be raised. Currently supported models and their corresponding token limits are:

- **gpt-3.5-turbo**: 4096 tokens
- **gpt-4**: 8192 tokens
- **gpt-4-32k**: 32768 tokens

**2. `cosine_distance(v1, v2)`:**

This function calculates the cosine distance between two vectors v1 and v2. It returns a scalar value that represents the similarity or distance between the two input vectors.

**3. `count_tokens(s: str, model_name: str) -> int`:**

This function accepts a string `s` and a model name, then returns the number of tokens in the string using the specified model's encoding.

**Hybrid Search Helper Functions:**

The following helper functions are used to facilitate a hybrid search operation:

**4. `sort_chunks_by_similarity(query_emb, vector_index)`:**

This function accepts a query embedding and a vector index (dictionary) containing embeddings and their associated texts. It calculates the cosine similarity between the query embedding and each embedding in the dictionary, then sorts these items in increasing order of similarity such that the most similar items are given precedence.

**5. `select_most_relevant_chunks(sorted_chunks, token_budget, model_name)`:**

This function takes the sorted chunks of text (from the previous function), a token budget and a model name as input. It iterates through the sorted chunks and adds them to the list of selected chunks until the specified token budget is reached or exceeded. As a result, the selected chunks will be the most relevant chunks of text within the token budget limit, based on their similarity to the query embedding.

The return value is a list of the selected chunks represented as strings.