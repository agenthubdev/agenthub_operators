# Markdown Documentation for HybridSearch Operator

## Summary
The HybridSearch Operator retrieves the most relevant chunks of text based on a given query and generates a response using ChatGPT.

## Inputs
- **vector_index**: Dictionary containing text embeddings as values that have already been processed and mapped using OpenAI's `neural_keys.compute_neural_key`. This input serves as the information source to search for relevant content with the given query.

## Parameters
- **query**: A string representing the question or query the user wants to get the response for.

## Outputs
- **hybrid_search_chatgpt_response**: A string containing the generated response from the ChatGPT combined with Hybrid Search.

## Functionality

### run_step
The `run_step` function is the core functionality of the HybridSearch Operator. It takes `step` and `ai_context` as input parameters and performs the following operations:
1. Extract the `query` from the input parameters.
2. Calculate the query embedding using `ai_context.embed_text(query)`.
3. Sort the input context chunks (from `vector_index`) by similarity to the query embedding using `sort_chunks_by_similarity()`.
4. Generate a prompt for ChatGPT using the query and most relevant chunks within token limits obtained using `select_most_relevant_chunks()`.
5. Run the chat completion on the generated prompt using `ai_context.run_chat_completion(prompt=prompt)`.
6. Set the output `'hybrid_search_chatgpt_response'` and add logs for debugging.

### Helper Functions
These functions are used within the `run_step` function to simplify various operations:

- **sort_chunks_by_similarity(query_emb, vector_index)**: This function takes the query embedding and the vector index as inputs and computes the similarity between the query embedding and the context chunks, then returns the context chunks sorted by similarity.

- **select_most_relevant_chunks(sorted_chunks, token_budget, model_name)**: This function selects and returns the most relevant chunks while adhering to the token budget constraint, ensuring that the total token count is within the allowed limit for the given model.

- **get_max_tokens_for_model(model_name)**: This function returns the maximum token limit for a given model name.

- **count_tokens(text, model_name)**: This function counts the number of tokens in a given text string for a specific model.