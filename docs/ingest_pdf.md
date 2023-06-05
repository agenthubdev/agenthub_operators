# IngestPDF

The **IngestPDF** class is an extension of the `BaseOperator` and focuses on ingesting PDF files either through a direct upload, a URL or from your local storage. It extracts the content from the PDF and provides output as plain text.

## Key Methods

- `declare_name()`: declares the name of the operator as 'Ingest PDF'
- `declare_category()`: sets the operator's category to 'CONSUME_DATA.value'
- `declare_allow_batch()`: returns `True` if batch processing is allowed
- `declare_parameters()`: defines and returns the required parameters such as 'pdf_uri', 'uploaded_file_name'
- `declare_inputs()`: defines the optional inputs such as 'file_name'
- `declare_outputs()`: defines the output key 'pdf_content' which is the extracted text from the PDF
- `run_step(step, ai_context)`: main function that extracts the content from the given PDF file
- `ingest(pdf_uri, file_name, uploaded_file_name, ai_context)`: ingests a PDF file from either direct upload, URL or from the local storage
- `is_url(pdf_uri)`: checks if the provided `pdf_uri` parameter is a valid URL
- `load_pdf_from_uri(url)`: loads the content of the PDF from a URL
- `load_pdf_from_storage(file_name, generated_this_run, ai_context)`: loads the content of the PDF from your local storage (either generated this run or not)
- `read_pdf(pdf)`: reads the content of the PDF and returns it as plain text

## Parameters

- `pdf_uri`: string, URL of the PDF file (optional)
- `uploaded_file_name`: string, the name of the PDF file previously uploaded to the workspace (optional)

## Inputs

- `file_name`: string, the name of the PDF file provided as input (optional)

## Outputs

- `pdf_content`: string, the extracted text from the PDF