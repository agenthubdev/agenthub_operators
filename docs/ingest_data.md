# **IngestData**

This class is used to consume data by ingesting content from a given URL and storing it in a variable. It inherits from the BaseOperator class and contains helper methods for scraping text from a URL.

## Inputs
- `input_url`: A string representing the URL to scrape text from.

## Parameters
- `data_uri`: A string representing the URL to scrape text from. If not provided, `input_url` is used instead.

## Outputs
- `uri_content`: A string representing the scraped text from the input URL.

## Helper Methods
- `is_url()`: A method that takes in a string and returns a boolean indicating whether the string is a valid URL or not.
- `scrape_text()`: A method that takes in a string representing a URL and returns the scraped text from that URL.

The `run_step()` method is called when the operator is executed. If `data_uri` is provided, it is used to scrape text. Otherwise, `input_url` is used. The scraped text is then stored in `uri_content`.  If a valid URL is not provided, nothing happens.

Note that the `is_url()` method is currently commented out due to issues during a demo.