# SplitData

**SplitData** is a class that inherits from `BaseOperator`. Its main goal is to **recursively split a given input text** into smaller chunks with a specified size and overlap. This is useful for processing large texts that require splitting before further processing.

### Inputs
- `text`: A string representing the input text to be split. 

### Parameters
- `chunk_size`: An integer specifying the desired size of each chunk. (Optional: Default is 2000)
- `chunk_overlap`: An integer specifying the desired amount of overlap between consecutive chunks. (Optional: Default is 100)

### Outputs
- `rts_processed_content`: A list of strings containing the split text chunks.

## Functionality

- `declare_name()`: Declares the operator name as 'Recursively Split Text'.
- `declare_category()`: Declares the operator category as 'MANIPULATE_DATA'.
- `declare_parameters()`: Declares the input parameters, `chunk_size` and `chunk_overlap`.
- `declare_inputs()`: Declares the input data, in this case, the `text` to be split. 
- `declare_outputs()`: Declares the output data, which is the split text, `rts_processed_content`.
- `run_step(step, ai_context)`: Takes the step and ai_context as input, processes the parameters, and sets the output. Also logs a success message.
- `process(params, ai_context)`: Takes the parameters and ai_context, gets the input text, and applies the `split()` method to the content.
- `split(params, ai_context, content)`: Takes the parameters, ai_context, and content, and splits the content into smaller chunks using the provided chunk_size and chunk_overlap.

The class utilizes the **RecursiveCharacterTextSplitter** from the `langchain.text_splitter` module to achieve the splitting process. The splitting is performed by creating an instance of the RecursiveCharacterTextSplitter class and using the `split_documents(content)` method to return the split texts.