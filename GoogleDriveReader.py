import re
from .base_operator import BaseOperator
from ai_context import AiContext
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveReaderOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Google Drive Reader Operator'

    @staticmethod
    def declare_description():
        return 'This operator can read any Google Drive file that is shared from a link.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "file_link",
                "data_type": "string",
                "placeholder": "Enter Google Drive file link",
                "description": "The link of the Google Drive file to be read"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "file_content",
                "data_type": "string",
                "description": "Content of the Google Drive file"
            }
        ]

    def run_step(self, step, ai_context):
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
        file_link = step['parameters']['file_link']
        file_id = re.search('(?<=d/)(.*)(?=/view)', file_link).group(0)
        file = drive.CreateFile({'id': file_id})
        file_content = file.GetContentString()
        ai_context.set_output('file_content', file_content, self)