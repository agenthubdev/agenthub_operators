# SplitData Operator Documentation

## Summary
The SplitData operator recursively splits the input text into smaller chunks based on the provided chunk size and overlap values.

## Inputs
- `text`: A string input that contains the text data to be split into smaller chunks.

## Parameters
- `chunk_size`: An integer value representing the size of each chunk the input text will be split into (Optional: Default is 2000).
- `chunk_overlap`: An integer value representing the overlap between consecutive chunks (Optional: Default is 100).

## Outputs
- `rts_processed_content`: A string output containing the smaller chunks of text after the splitting process.

## Functionality
The `run_step` function processes the operator parameters, splits the input text into smaller chunks using the `split` function, and sets the output value. It also adds a log entry for the successful text splitting.

The `process` function fetches the input text and calls the `split` function, which formats and returns the text chunks.

The `split` function retrieves the chunk size and overlap values from the parameters, converts them into integers, and initializes a `RecursiveCharacterTextSplitter` object. The `split_documents` function of the `text_splitter` object is then used to split the content into smaller chunks based on the provided chunk size and overlap. The resulting text chunks are returned.