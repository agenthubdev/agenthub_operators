# IngestPDF Operator Documentation

## Summary

The IngestPDF operator is an AI operator that takes a PDF as input, either as a URI or a user-uploaded file, and converts it into a text blob.

## Inputs

- `pdf_uri`: A string that contains the URL of the PDF (optional)
- `uploaded_file_name`: A string that contains the name of the uploaded PDF file (optional)

## Parameters

- `pdf_uri`: A string that indicates the URL of the PDF (placeholder: "Enter the URL of the PDF")
- `uploaded_file_name`: A string that indicates the name of the uploaded PDF file (placeholder: "Enter the name.pdf of the uploaded PDF")
- (Commented out) `pdf_parsing_method`: A string that indicates the method of parsing PDF, with a default value of "tabula" for preservation of tables and spreadsheets

## Outputs

- `pdf_content`: A string that is a blob of text representing the content of the input PDF

## Functionality

The operator's main function is `run_step`, which takes the following arguments:

- `step`: The step defined in the AI workflow
- `ai_context`: An instance of the AiContext class, which helps the operator manage inputs, outputs, and other information

The `ingest` helper function is responsible for loading the PDF either from given URL (`pdf_uri`) or from the workspace's storage where it was uploaded by the user (`uploaded_file_name`). The content from the URL or uploaded PDF file is then scraped, with appropriate log messages being added.

The following helper functions are there to perform specific tasks:

- `is_url`: Determines if the given string is a URI and returns a boolean value
- `load_pdf_from_uri`: Takes a URL and returns a PDF file from it
- `load_pdf_from_storage`: Loads a PDF file from the storage, either with a given run_id (if generated during this AI run) or without one
- `read_pdf`: Reads the content of the input PDF and converts it into a string using tabula Python library to preserve tables and spreadsheets formatting

When the PDF content has been processed, the output `pdf_content` is set, and the operator returns the blob of text.