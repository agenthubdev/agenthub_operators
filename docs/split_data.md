# SplitData

**SplitData** is a class derived from `BaseOperator` which is responsible for recursively splitting a given text into multiple chunks. The main functionality is implemented within the `split` helper method, which takes the user-defined `chunk_size` and `chunk_overlap` as input parameters and splits the text into chunks accordingly.

## Inputs

- `text`: A string representing the input text that needs to be split.

## Parameters

- `chunk_size`: An integer which determines the maximum size of each chunk (Optional, default is 2000).
- `chunk_overlap`: An integer which determines the number of overlapping characters between adjacent chunks (Optional, default is 100).

## Outputs

- `rts_processed_content`: A list of strings representing the split text chunks.

## Helper Methods

### run_step(self, step, ai_context: AiContext)

This method is responsible for processing the inputs and parameters, and then calling the `process` method to split the text. Once the text has been split, it adds the result to the AI context and logs a success message.

### process(self, params, ai_context)

This method takes `params` and `ai_context` as input and then retrieves the input text using `ai_context.get_input()`. It then calls the `split` method to split the text into chunks.

### split(self, params, ai_context, content)

This method takes `params`, `ai_context`, and `content` as input and extracts the `chunk_size` and `chunk_overlap` values. If these values are not provided, it defaults to 2000 and 100, respectively. An instance of `RecursiveCharacterTextSplitter` is then created with the provided chunk size and overlap parameters. Finally, the `split_documents()` method of this text splitter object is called with the content to generate the desired chunks.

So, by using the **SplitData** class, one can easily and efficiently split a large text into smaller chunks with user-defined size and overlap values.