# IndexData Operator

## Summary
This operator indexes input text data into embeddings for further processing and analysis.

## Inputs
- `text`: A string input containing the text data to be indexed.

## Parameters
This operator does not have any parameters.

## Outputs
- `vector_index`: A dictionary containing the embeddings of the indexed text data as keys and the corresponding chunks of text as values.

## Functionality

### `run_step`
The main function of this operator is `run_step`, which takes two parameters:
- `step`: The current step of the pipeline.
- `ai_context`: The AI context object to interact with the underlying model and data.

It performs the following tasks:
- Gets the input text and cleans it by removing newlines characters.
- Gets the embeddings of the text using the `len_safe_get_embedding` function.
 - Sets the output `vector_index` for the operator.
- Logs the completion of indexing with the number of chunk embeddings generated.

### Helper Functions

#### `clean_text`
This function takes in a text input and replaces newline characters with spaces.

#### `batched`
This function takes in an iterable and a batch size (n), and yields batches of the iterable with the specified size.

#### `chunked_tokens`
This function takes in a text, encoding name, and chunk length, and breaks the text into chunks based on the provided parameters. It uses Tiktoken for encoding and decoding the tokens.

#### `len_safe_get_embedding`
This function is responsible for generating embeddings for the given text, provided with a specified maximum token length and an encoding name. It iterates through the chunks obtained from `chunked_tokens` and generates an embedding for each chunk. It returns a dictionary containing the embeddings as keys and the corresponding chunks of text as values.