# IngestPDF

**IngestPDF** is a class that extends **BaseOperator**. The main goal of this class is to ingest PDF files and extract their content, which can be done through three different sources:
1. An uploaded file through the `uploaded_file_name` parameter.
2. A file previously generated in the current run, passed as input with the name `file_name`.
3. A PDF file from a specified URL using the `pdf_uri` parameter.

When executing the `run_step()` method, it tries to ingest the PDF file from the mentioned sources in the specific order and extracts the content of the PDF file. 

## Inputs
- `file_name` (optional, string): Represents the name of the PDF file that was previously generated during the current run.

## Parameters
- `pdf_uri` (string): Represents the URL of the PDF file to be ingested.
- `uploaded_file_name` (string): Represents the name of the previously uploaded PDF file.

## Outputs
- `pdf_content` (string): Contains the extracted content of the PDF file.

## Helper Methods

- `ingest(self, pdf_uri, file_name, uploaded_file_name, ai_context)`: Takes the PDF file information and extracts its content.
- `is_url(self, pdf_uri)`: Checks if the provided `pdf_uri` is a valid URL.
- `load_pdf_from_uri(self, url)`: Downloads a PDF file from the given URL.
- `load_pdf_from_storage(self, file_name, generated_this_run, ai_context)`: Loads a PDF file from storage, either from a previous run or the current run.
- `read_pdf(self, pdf)`: Reads the content of a PDF file using Tabula, which extracts tables and formulates them into a readable string format. The text is then returned as a single string.