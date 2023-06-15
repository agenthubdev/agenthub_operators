**Class: Summarize**

The `Summarize` class is a **BaseOperator** that handles the summarization of content using OpenAI's GPT-3. It handles both the setup and communication with the GPT-3 API and provides a simple, extendable interface for `AiContext` to make use of.

- Inputs: 
  * `rts_processed_content`: A **string** representing the content to be summarized.
- Parameters: 
  * `temperature`: A **float** used to adjust the GPT-3 output. A lower value results in more focused output. Default: 0.2.
- Outputs: 
  * `summarize_gpt_response`: The **string** response from GPT-3, containing the summarized content.

**Main Methods:**

- `declare_*()`: A series of `declare` methods that define the name, category, parameters, inputs, and outputs of the `Summarize` operator.

- `run_step(self, step, ai_context)`: This method is responsible for running the summarization using the provided `step` and `AiContext`. It firstly acquires the parameters (like `temperature`) and passes them along with the data to be summarized to the `process()` method. It then stores the GPT-3 response as an output in the `AiContext`.

- `process(self, params, ai_context)`: This method is solely responsible for handling the actual communication with OpenAI's GPT-3. It calls the `chain()` method, passing in the `params`, data to be summarized, and the OpenAI API key.

- `chain(self, params, data, openai_api_key)`: This method sets up the **ChatOpenAI** instance `llm` with the proper `temperature` and OpenAI API key. It loads the summarization chain (`load_summarize_chain()`) and then runs it on the provided data, returning the GPT-3 response as a **string**.

By providing a clear interface for handling GPT-3 summarization, this class greatly simplifies the process of integrating summarization within an AI-driven workflow.