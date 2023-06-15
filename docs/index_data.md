# IndexData

**IndexData** is a class that extends the **BaseOperator** class and is responsible for indexing data. It takes text as input, cleans it, and generates an embeddings dictionary that represents the vector index of the text. 

The class has the following methods:

- **declare_name** : Returns the name 'Index Data'.
- **declare_category** : Returns the category, in this case 'Manipulate Data'.
- **declare_parameters** : Returns an empty list, as there are no parameters required.
- **declare_inputs** : Returns a single input 'text' which is of data type 'string'.
- **declare_outputs** : Returns a single output 'vector_index' which is of data type '{}', a dictionary.
- **run_step** : Main method that takes an `AiContext` as argument and performs the actual indexing, cleaning, and generation of the embeddings dictionary.
- **clean_text** : Cleans the input text to ensure proper formatting.
- **batched** : A helper function that will batch an iterable in chunks of size `n`.
- **chunked_tokens** : A generator that yields text chunks as strings, keeping each chunk within a specified token length.
- **len_safe_get_embedding** : Retrieves a dictionary of embeddings for text chunks provided. 

The constants **EMBEDDING_CTX_LENGTH** and **EMBEDDING_ENCODING** are set to `1000` and `'cl100k_base'` respectively. This means that each chunk of text will be limited to 1000 tokens. The choice of 1000 tokens was made to find a balance between speed and accuracy, as a small query could fit 4 chunks in the context.