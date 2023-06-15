# IngestData Class

The **IngestData** class is a subclass of the _BaseOperator_, designed to consume and process data from a given URL. It scrapes the textual content of the URL and returns it as a clean string. 

## Key Sections

- **declare_name**: Returns the name 'Ingest Data' for this operator.
- **declare_category**: Returns the OperatorCategory.CONSUME_DATA enumeration value as the operator category.
- **declare_parameters**: Defines the list of parameters for this operator. The only parameter is "data_uri", a string representing the URL to browse.
- **declare_inputs**: Defines the list of inputs for this class. The only input is "input_url", a string representing the input URL.
- **declare_outputs**: Defines the list of outputs for this class. The only output is "uri_content", a string representing the scraped content from the URL.

## Helper Methods

- `run_step(self, step, ai_context: AiContext)`: Executes the ingestion process based on the provided parameters and AI context.

- `ingest(self, params, ai_context)`: Ingests the data from the given URL and stores it in the AI context.

- `is_url(self, data_uri)`: Quick, hacky workaround to determine if the data_uri is a URL.

- `scrape_text(self, url)`: Scrapes the text from the given url using BeautifulSoup and removes any script or style tags, returning the cleaned text.

**Note**: The main functionality of the class revolves around the _ingest_ method, which first checks if the data URI is a URL using the is_url helper method. Then, it scrapes the content from the URL using the scrape_text helper method, and stores the results in the AI context, finally adding a log entry indicating that the content has been scraped.