# IndexData

**IndexData** is a class that is responsible for indexing input text data. It takes in a text string as an input, splits it into chunks of a set token length (1000 in this case), and creates an embedding vector for each chunk. The class outputs a dictionary with the embedding vectors as keys and the corresponding text chunks as values.

The `run_step` method of IndexData takes in a `text` input and processes it by removing all newline characters. The `clean_text` method performs this cleaning task.

The `len_safe_get_embedding` method of IndexData is responsible for generating the embedding vectors for each chunk of text, and storing the embeddings in a dictionary along with the corresponding chunk. The chunks of text are created by calling the `chunked_tokens` method, which chunks the input text into pieces of a set token length using the `batched` method to batch the tokens and the `decode` method to decode the resulting chunks. The `embed_text` method is then used to generate the embedding vectors for each chunk.

The inputs for this class are a `text` input, which is a string of text to be indexed, and there are no parameters. The output is a dictionary named `vector_index`, with the embedding vectors as keys and the corresponding text chunks as values.

In summary, IndexData is a class that takes in an input text data and generates embedding vectors for each chunk of text, which are then stored in a dictionary for indexing purposes.