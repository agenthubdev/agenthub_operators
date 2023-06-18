# **Hybrid Search Helpers**

This code snippet is a collection of helper functions that can be used for hybrid search algorithms. These functions can be used to sort text chunks by similarity to a query, select the most relevant chunks based on a given token budget, and count the number of tokens in a given string.

## get_max_tokens_for_model

This function returns the maximum number of tokens that a given language model can handle. It takes in a string argument called `model_name`, which is the name of the target language model. 

### Inputs:
- `model_name` (str): The name of the target language model. 

### Outputs:
- `max_tokens` (int): The maximum number of tokens that the target language model can handle.

## cosine_distance

This function computes the cosine distance between two vectors. It takes in two vector arrays, `v1` and `v2`. 

### Inputs:
- `v1` (array): The first vector array
- `v2` (array): The second vector array

### Outputs:
- `distance` (float): The cosine distance between `v1` and `v2`

## count_tokens

This function counts the number of tokens in a given string, using a language model's encoding. It takes in two arguments: a string `s` and a model name `model_name`.

### Inputs:
- `s` (str): The string to count tokens for
- `model_name` (str): The name of the language model to use for encoding

### Outputs:
- `num_tokens` (int): The number of tokens in `s`, as encoded by the language model

## sort_chunks_by_similarity

This function sorts a list of text chunks by their similarity to a query vector. It takes in a query embedding vector `query_emb` and a dictionary of text chunks with their corresponding embedding vectors `vector_index`.

### Inputs:
- `query_emb` (array): The query embedding vector
- `vector_index` (dict): A dictionary of text chunks with their corresponding embedding vectors

### Outputs:
- `chunks` (list): A list of text chunks sorted in decreasing order of similarity to `query_emb`.

## select_most_relevant_chunks

This function selects the most relevant chunks from a list, based on a given token budget and a language model. It takes in a sorted list of text chunks `sorted_chunks`, a token budget `token_budget`, and a language model name `model_name`.

### Inputs:
- `sorted_chunks` (list): A list of text chunks sorted in decreasing order of similarity
- `token_budget` (int): The maximum number of tokens to spend
- `model_name` (str): The name of the language model to count tokens with

### Outputs:
- `selected_chunks` (list): A list of the most relevant text chunks selected based on `token_budget` and `model_name`.