import io
from .base_operator import BaseOperator
from ai_context import AiContext

class FileUploadOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'File Upload Operator'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "file_content",
                "data_type": "string",
                "placeholder": "Enter the file content",
                "description": "File content to be uploaded"
            },
            {
                "name": "file_name",
                "data_type": "string",
                "placeholder": "Enter the file name",
                "description": "Name of the file to be uploaded"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "file_content",
                "data_type": "string",
                "description": "File content to be uploaded",
                "optional": "1"
            },
            {
                "name": "file_name",
                "data_type": "string",
                "description": "Name of the file to be uploaded",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "upload_status",
                "data_type": "string",
                "description": "Status of the file upload"
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        params = step['parameters']
        file_content = params.get('file_content') or ai_context.get_input('file_content', self)
        file_name = params.get('file_name') or ai_context.get_input('file_name', self)

        if file_content and file_name:
            ai_context.add_to_log(f"Uploading file {file_name} to storage.")
            self.upload_file(file_content, file_name, ai_context)
        else:
            ai_context.set_output('upload_status', 'Failed: Missing file content or file name.', self)
            ai_context.add_to_log("No file content or file name provided.")

    def upload_file(self, file_content, file_name, ai_context):
        file_data = io.StringIO(file_content)
        ai_context.put_file(file_name, file_data)
        ai_context.set_output('upload_status', 'Success: File uploaded.', self)
        ai_context.add_to_log(f"File {file_name} uploaded successfully.")