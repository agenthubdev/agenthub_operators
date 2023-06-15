# HybridSearch

The **HybridSearch** class is a base operator that combines vector similarity search with the ChatGPT model to generate more relevant responses. In general, it enables generating contextual responses by utilizing input textual data.

## Main Components
1. **declare_name**: 'Hybrid Search'
2. **declare_category**: BaseOperator.OperatorCategory.AI.value
3. **declare_parameters**: 'query' (string)
4. **declare_inputs**: 'vector_index' (JSON)
5. **declare_outputs**: 'hybrid_search_chatgpt_response' (string)

### General Purpose

The main functionality of this class is to:
1. Utilize the given `query`, its embedding, and `vector_index` input for processing.
2. Sort the chunks of text by similarity and block through the `sort_chunks_by_similarity` and `select_most_relevant_chunks` utility methods.
3. Create a prompt and generate an AI response using ChatGPT with the context of the selected chunks.
4. Set the output as 'hybrid_search_chatgpt_response' containing the AI-generated response.

### Helper Methods

- `sort_chunks_by_similarity`: Sort the text chunks based on their similarity to the query embedding.
- `select_most_relevant_chunks`: Select the most relevant chunks within the token budget.
- `get_max_tokens_for_model`: Acquire the maximum token limit for the specified model.
- `count_tokens`: Count the number of tokens in a given text for a specific model.