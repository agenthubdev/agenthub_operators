# ChatBot

**ChatBot** is a class that inherits from `BaseOperator`. This class is used to connect with a chatbot model, receive a user query, and provide an appropriate response based on the conversation history and a vector index.

## Class Methods

Here are the main methods of the **ChatBot** class:

- `declare_name()`: Returns the name of the operator as 'Ask Chat Bot'.
- `declare_category()`: Returns the operator category as AI.
- `declare_description()`: Provides a brief description of the class functionality.
- `declare_parameters()`: Specifies the required parameters for the class which include `vector_index_id` and `query`.
- `declare_inputs()`: This operator does not accept any inputs.
- `declare_outputs()`: Defines the output as `response` with a data type of string.
- `run_step()`: Executes the main functionality of the ChatBot, which includes:
  - Retrieving the query parameter and model name.
  - Embedding the text of the query.
  - Getting the vector index based on the passed ID.
  - Limiting the tokens for the model to prevent exceeding the token limit.
  - Incorporating hybrid search results into the prompt.
  - Loading chat history up to the token budget allowed.
  - Running the chat completion based on the conversation history and user query.
  - Storing the chatbot response as an output and adding it to the conversation log.

## Parameters

- `vector_index_id`: A unique string identifier for the persisted vector index, usually printed by Persist Vector Index.
- `query`: A string containing the user's question for the chatbot.

## Inputs

This class does not require any inputs.

## Outputs

- `response`: A string containing the chatbot's response to the user query.

## Functionality

The main purpose of the **ChatBot** class is to interact with a chat model, process user queries, and provide suitable responses based on the conversation context. The class uses helper methods to include context from a hybrid search (using a vector index), manage token limits, and load conversation history into the chat model.

When run, the `run_step()` method takes the input parameters, processes the query, and generates a chatbot response. The response is then stored as an output and added to the conversation log.

In summary, the **ChatBot** class combines conversation history with a relevant embedded context to provide an appropriate response based on the user query.