# Hybrid Search

This class implements a hybrid search functionality by combining the results of semantic search and generative chatbot models. The `run_step` method takes a query and an index of precomputed document embeddings as inputs. It then uses `sort_chunks_by_similarity` to find chunks of text that are most similar to the query and `select_most_relevant_chunks` to select the most relevant chunks for the given prompt length. The method constructs a prompt by appending the selected chunks to the query and passes it to `ai_context.run_chat_completion` method to generate a response. Finally, the response is set as output and logged.

**Inputs:** 
- `vector_index`: precomputed document embeddings for the search index.

**Parameters:**
- `query`: the query string.

**Outputs:**
- `hybrid_search_chatgpt_response`: the response of the generative chatbot.

Helper methods:
- `sort_chunks_by_similarity`: sorts the chunks of text by their similarity scores with respect to the query.
- `select_most_relevant_chunks`: returns the most relevant chunks within a token budget.
- `count_tokens`: returns the number of tokens required to generate a text using the given GPT model.
- `get_max_tokens_for_model`: returns the maximum number of tokens that can be used by the given GPT model. 

The hybrid approach aims to benefit from the strengths of both search and generative models by reducing the search space while also taking into account the context. The method allows for more flexibility in generating responses while also improving the response quality by selecting the most relevant chunks.