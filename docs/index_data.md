# IndexData

**Index Data** is a class that extends the `BaseOperator` and is responsible for indexing the input text into chunk embeddings. This can be useful when dealing with large texts and requiring efficient operations on text data.

The main function of this class is `run_step`, which takes the input text, cleans it, and generates the vector index by generating embeddings for chunks of the text. The class also includes helper methods to clean text, create batches, and generate chunks for processing.

## Parameters

The `IndexData` class does not require any parameters.

## Inputs

- `text`: A string that represents the text to be processed and indexed.

## Outputs

- `vector_index`: A dictionary containing the vector index of the text, where each key is a string representation of the embedding vector, and the value is the corresponding chunk of text.

## Helper Methods

- `clean_text(self, text)`: Removes newline characters from the input text and returns the cleaned text.

- `batched(self, iterable, n)`: Yields batches of size `n` from an iterable.

- `chunked_tokens(self, text, encoding_name, chunk_length)`: Yields chunks of size `chunk_length` for a given input text and encoding_name. This method uses the `batched()` method to create chunks and the `tiktoken` library to handle the encoding.

- `len_safe_get_embedding(self, text, ai_context, max_tokens=EMBEDDING_CTX_LENGTH, encoding_name=EMBEDDING_ENCODING)`: Generates chunk embeddings for the input text. It divides the input text into chunks by calling the `chunked_tokens()` method, gets the embeddings for each chunk using the `ai_context.embed_text()` method, and creates a dictionary with tuple(embedding) as keys and the corresponding chunks as values.