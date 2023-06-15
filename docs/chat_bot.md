# ChatBot

**ChatBot** is a class that extends *BaseOperator* and provides an implementation to answer questions using a given *vector_index_id* and conversation history. It incorporates results of hybrid search and chat history into the AI-generated response.

### Inputs
- None

### Parameters
- **vector_index_id**: A string indicating the Vector Index Id.
- **query**: A string representing the question to ask the ChatBot.

### Outputs
- **response**: A string containing the AI-generated response.

The `run_step()` method is the core functionality of the ChatBot class. In this method, the following steps are performed:

1. Retrieve the query and vector index from the given parameters.
2. Calculate token limits based on the model name.
3. Retrieve the most relevant chunks from the vector index and incorporate them into the prompt.
4. Load chat history and append the prompt containing the generated context.
5. Run the AI chat completion to generate a response.
6. Store the user's query and AI response in the chat history memory.

The purpose of the helper methods is as follows:

- `sort_chunks_by_similarity()`: Sorts chunks based on their similarity to the query embedding.
- `select_most_relevant_chunks()`: Selects the most relevant chunks within the given token budget.
- `get_max_tokens_for_model()`: Returns the maximum tokens allowed for the given model name.
- `count_tokens()`: Counts the number of tokens in the text based on the model name.