# Summarize Content Operator

## Summary
This operator provides functionality to summarize given content using OpenAI powered language models.

## Inputs
- `rts_processed_content`: A string input representing the content that needs to be summarized.

## Parameters
- `temperature`: A float parameter representing the "temperature" used by the language model during text generation. A higher temperature will result in more randomness, and a lower temperature will produce more focused and deterministic outputs. Default value is 0.2.

## Outputs
- `summarize_gpt_response`: A string output representing the summarized content returned by the GPT model.

## Functionality
The main function in this operator is `run_step`, which takes the following arguments:

- `step`: The step in the execution workflow.
- `ai_context`: An instance of the AiContext class, which provides helpful methods and data objects.

1. The `run_step` function processes the provided input parameters by calling the `process` function.
2. It communicates with the GPT model using the `ChatOpenAI` class and configures it with the provided `temperature` and OpenAI API key.
3. It then loads the appropriate summarization model using the `load_summarize_chain` function by passing the AI model instance and specifying the chain type as "map_reduce".
4. The text summarization model is executed with the input data, and the response is returned.
5. Finally, the output is set in AI context as `summarize_gpt_response` and a log message is added with the GPT response.

In summary, this operator uses GPT-based models to summarize input texts, allowing developers to leverage powerful language models for natural language processing tasks.