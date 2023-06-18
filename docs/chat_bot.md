# Chat Bot Operator Markdown Documentation

## Summary

A Chat Bot operator that answers questions using a given vector index and the conversation history of the current user.

## Inputs

There are no inputs to this operator.

## Parameters

- `vector_index_id` (string): The unique identifier of the vector index, used for embedding and searching. Typically printed by Persist Vector Index.
- `query` (string): The user's question to be answered by the chat bot.

## Outputs

- `response` (string): The chat bot's answer to the user's question.

## Functionality

### `run_step`

The `run_step` function follows the given steps:

1. Extract parameters from the step dictionary.
2. Embed the query text and obtain the model name.
3. Retrieve the vector index using the vector index ID.
4. Set token limits and budgets for different parts of the prompt.
5. Incorporate the results of the Hybrid search into the prompt:
    - Sort chunks by similarity to the query.
    - Select the most relevant chunks and add them to the prompt as context.
6. Load chat history up to `chat_history_token_budget`:
    - Retrieve chat history from memory.
    - Make an AI response using the combined prompt and the chat history.
    - Store the AI response as the output ("response").
7. Add the user query and system response to chat history.

### Helper Functions

The `run_step` function is supported by the following helper functions:

- `sort_chunks_by_similarity`: Sorts chunks stored in a vector index by their similarity to the query embedding.
- `select_most_relevant_chunks`: Selects the most relevant chunks based on their similarity and the budget to fit in the prompt.
- `get_max_tokens_for_model`: Returns the maximum number of tokens allowed for a given model.
- `count_tokens`: Counts tokens in a given text, considering the model's specifications.