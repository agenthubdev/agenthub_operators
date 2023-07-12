import io
import json
import csv

import tabula
import pandas as pd
from PyPDF2 import PdfReader

from ai_context import AiContext
from .base_operator import BaseOperator


class FileReader(BaseOperator):
    @staticmethod
    def declare_name():
        return 'File Reader'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.CONSUME_DATA.value

    @staticmethod
    def declare_description():
        return "Reads the content from an uploaded file and returns a string of the file's contents. Supports .pdf, .json, and, .csv filetypes"

    @staticmethod
    def declare_allow_batch():
        return True

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "uploaded_file_name",
                "data_type": "string",
                "placeholder": "Ex. example.pdf",
                "description": "Enter the name + extension of the uploaded file"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "uploaded_file_name",
                "data_type": "string",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "file_contents",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        params = step['parameters']

        param_file_name = params.get('uploaded_file_name')
        input_file_name = ai_context.get_input('uploaded_file_name', self)

        uploaded_file_name = param_file_name or input_file_name

        self.ingest(uploaded_file_name, ai_context)

    def ingest(self, uploaded_file_name, ai_context):
        if uploaded_file_name:
            ai_context.add_to_log(
                f"Loading {uploaded_file_name} from storage.")

            file_data = self.load_file_from_storage(
                uploaded_file_name, ai_context)

            text = self.read_file(file_data, uploaded_file_name)

            ai_context.set_output('file_contents', text, self)
            ai_context.add_to_log(
                f"Content from uploaded file {uploaded_file_name} has been scraped.")
        else:
            ai_context.set_output('file_contents', '', self)
            ai_context.add_to_log("No file or content to read.")

    def load_file_from_storage(self, file_name, ai_context):
        file_data = ai_context.get_file(file_name)
        return file_data

    def read_file(self, file_data, file_name):
        if file_name.lower().endswith('.pdf'):
            return self.read_pdf(file_data)
        elif file_name.lower().endswith('.json'):
            data = json.loads(file_data.decode())
            json_str = json.dumps(data, indent=4)
            return json_str
        elif file_name.lower().endswith('.csv'):
            text_data = file_data.decode('utf-8')
            reader = csv.reader(text_data.splitlines())
            data = [cell for row in reader for cell in row]
            return ','.join(data)
        else:
            raise ValueError(f"Unsupported file format: {file_name}")

    def read_pdf(self, pdf):
        pd.set_option('display.max_colwidth', None)
        pdf_content = io.BytesIO(pdf)
        df_list = tabula.read_pdf(pdf_content, pages='all')

        # If tabula returned empty DataFrames, fall back to PyPDF2
        if all(df.empty for df in df_list):
            pdf_reader = PdfReader(pdf_content)
            text = []
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text.append(page.extract_text())
            return "\n".join(text)

        pdf_content = "\n".join(df.to_string(index=False) for df in df_list)
        return pdf_content
