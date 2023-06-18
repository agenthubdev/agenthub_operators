## **SplitData**

This class is responsible for splitting text data into smaller chunks to improve processing efficiency. The class takes in a single input parameter, `text`, which is the text data to be split. The outputs of this class are the split texts stored under the `rts_processed_content` key.

The class has two parameters:
- `chunk_size`: an integer value representing the chunk size (default is 2000).
- `chunk_overlap`: an integer value representing overlap of text between chunks (default is 100).

To split text, the `split()` method is called passing in the input text and the parameters. The method uses the RecursiveCharacterTextSplitter class to split the text into smaller chunks. The `process()` method calls the `split()` method and returns the formatted text.

In the `run_step()` method, the input parameters are processed, and the `rts_processed_content` output is set. The `ai_context` object is used to manage the inputs and outputs of the operator.

This class can be used as part of a larger text processing pipeline to split large text data into smaller chunks for easy processing.