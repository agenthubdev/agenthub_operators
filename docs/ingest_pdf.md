# **IngestPDF**

This class is a subclass of the **BaseOperator** class and is used to convert a PDF file to a blob of text. The PDF file can be either a URI or a file that the user uploaded to their workspace on AgentHub. 

## Inputs
There are two optional input parameters: **pdf_uri** and **uploaded_file_name**. **pdf_uri** takes a string value representing the URL of the PDF to be ingested. **uploaded_file_name** represents the name of the uploaded PDF to be ingested.

## Parameters
There are two parameters, **pdf_uri** and **uploaded_file_name**. Both take string values and can be optionally passed as inputs.

## Outputs
The class has one output parameter: **pdf_content**, which is a string representing the text content of the ingested PDF.

## Methods
### `ingest(self, pdf_uri, uploaded_file_name, ai_context)`
This method handles the ingestion of the PDF file and reads its content. Depending on the input parameters, it loads the PDF file either from a URL or from storage. It then reads the content of the PDF file using the **read_pdf** helper method and sets the output parameter **pdf_content**.

### `load_pdf_from_uri(self, url)`
This method loads the content of the PDF file from a URL.

### `load_pdf_from_storage(self, file_name, generated_this_run, ai_context)`
This method loads the content of the PDF file from storage. It takes in a boolean value, **generated_this_run**, that indicates if the file was generated in the current run.

### `read_pdf(self, pdf)`
This method reads the content of the PDF file and returns it as a string. It uses the **tabula.read_pdf** method to read the content.