# IngestData

**IngestData** is a class that extends the `BaseOperator` class. Its primary purpose is to consume data, either from a provided URL or from a file, and make it available for further processing.

## Class Methods

- `declare_name()`: This method declares the name of the operator as "Ingest Data".
- `declare_category()`: This method declares the category of the operator as "CONSUME_DATA".
- `declare_parameters()`: This method declares the parameters that this operator accepts, which is an array containing a dictionary with the key "data_uri", and its corresponding data type as "string".
- `declare_inputs()`: This method declares the inputs this operator works with, which is an array containing a dictionary with the key "input_url", and its corresponding data type as "string".
- `declare_outputs()`: This method declares the outputs that this operator produces, which is an array containing a dictionary with the key "uri_content", and its corresponding data type as "string".

## Helper Methods

- `is_url(data_uri)`: This method checks if the given `data_uri` is a valid URL or not. It does this by using a regular expression pattern. Currently, it returns `True` for all inputs as a temporary workaround.
- `scrape_text(url)`: This method takes a URL, uses `requests` to fetch the content of the website, and then removes any unnecessary tags such as scripts and styles using `BeautifulSoup`. The method then returns the scraped text with all unnecessary tags removed.

## Main Functionality

The main functionality of this class is within the `run_step()` and `ingest()` methods.

- `run_step(step, ai_context)`: This method takes the step configuration and the AI context, and calls the `ingest()` method to process the data.
- `ingest(params, ai_context)`: This method is responsible for ingesting the data from the given URL or file. It checks if the `data_uri` parameter is provided; if not, it fetches the input URL from the AI context. The ingested URL is then stored in the AI context's storage. It checks if the provided link is a URL using the `is_url()` helper method, and if it is, it scrapes the text using the `scrape_text()` helper method. The scraped text is then set as the output with the key name "uri_content", and a log is added with the message "Content from {data_uri} has been scraped.".