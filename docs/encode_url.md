# EncodeURL

The **EncodeURL** class is a subclass of `BaseOperator` that helps in **encoding URL strings**. It does not require any additional parameters and supports batch processing. The main purpose of this class is to encode input strings to make them URL-friendly.

**Inputs:**
- `input`: A string to be encoded for use in a URL.

**Outputs:**
- `encoded_url`: The encoded URL-friendly version of the input string.

## Key Methods

- `declare_name()`: This method returns the name of the class as 'EncodeURL'.
- `declare_category()`: This method returns the category of the class as `MANIPULATE_DATA`.
- `declare_parameters()`: This method returns an empty list, indicating that no additional parameters are required for this class.
- `declare_allow_batch()`: This method returns `True`, meaning that this operator allows batch processing.
- `declare_inputs()`: This method defines the inputs for the class, which includes the input string to encode.
- `declare_outputs()`: This method defines the outputs for the class, which includes the encoded URL.
- `run_step(step, ai_context: AiContext)`: This method handles the main functionality of the *EncodeURL* class. It retrieves the input string, encodes it using the `quote_plus` function from the `urllib.parse` module, and stores the encoded URL in the output.

In summary, the **EncodeURL** class is designed to efficiently and effectively convert input strings into URL-friendly encoded strings, making it easy to work with URLs in your projects.