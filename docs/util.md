# Markdown Documentation

## Summary
This code provides a set of helper functions for managing and interacting with OpenAI language models, specifically in the task of ranking and selecting relevant text chunks based on computed similarity and token constraints.

## Inputs
- `model_name (str)`: The name of the OpenAI language model.
- `s (str)`: A text string to be evaluated.
- `query_emb (array)`: The query embedding for which similarity is to be calculated.
- `vector_index (dict)`: A dictionary containing embeddings and their corresponding text chunks.
- `token_budget (int)`: The maximum number of tokens that can be included in the resultant selected chunks.

## Parameters
- `emb_tuple`: Tuple containing the precomputed embeddings of the text.
- `text`: The text chunk corresponding to the precomputed embeddings.
- `similarity`: The computed similarity score between the query embedding and the text chunk embeddings.
- `token_limits`: A dictionary that maps model names to their maximum token limits.

## Outputs
- `max_tokens (int)`: The maximum token limit for a specific model.
- `cosine_dist (float)`: The cosine similarity between two input vectors.
- `num_tokens (int)`: The number of tokens in a given text string according to a given language model.
- `selected_chunks (list)`: A list containing the chosen text chunks based on similarity and token constraints.

## Functionality
- `get_max_tokens_for_model(model_name)`: Returns the maximum token limit for a specified language model.
- `cosine_distance(v1, v2)`: Computes the cosine similarity between two input vectors.
- `count_tokens(s, model_name)`: Counts the number of tokens in a given text string according to a specified language model.
- `sort_chunks_by_similarity(query_emb, vector_index)`: Sorts the text chunks in the vector index based on their computed similarity to the given query embedding.
- `select_most_relevant_chunks(sorted_chunks, token_budget, model_name)`: Selects the most relevant text chunks based on similarity and token constraints, ensuring the total token count remains within the specified token_budget.