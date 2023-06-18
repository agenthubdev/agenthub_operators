# Ingest Data Operator
This code defines an IngestData operator that scrapes a given URL and returns the web page content.

## Summary
Ingest Data operator reads a URL (web page) and returns its content as plain text.

## Inputs
- `input_url` (optional): A URL provided as an input to the operator which can be used instead of the `data_uri` parameter.

## Parameters
- `data_uri` (string): A URL to be scraped and its content to be ingested by the operator.

## Outputs
- `uri_content` (output): Data type string. The content of the ingested web page returned as plain text with unnecessary elements removed (e.g., line breaks, spaces, and HTML text).

## Functionality
The main functionality is encapsulated in the `run_step` method which:
- Fetches the input from the user.
- Calls the `ingest` function which scrapes the content of the given URL.
- Sets the output 'uri_content' to the scraped text.

There are three supporting helper functions inside the class IngestData:
- `ingest`: Given the URL and AiContext object, ingests the content by calling the `scrape_text` function and stores the result in the output object.
- `is_url`: Returns True if the given URL matches a URL pattern. Currently a workaround is applied that makes it always return True.
- `scrape_text`: Scrapes the provided URL and returns the web page text content with unnecessary parts removed.