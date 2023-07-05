import re
from .base_operator import BaseOperator
from ai_context import AiContext

class CodeRevisionOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Code Revision Operator'

    @staticmethod
    def declare_description():
        return 'This operator takes a text string of code and generates a revised version based on user input.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "code",
                "data_type": "string",
                "placeholder": "Enter original code",
                "description": "Original code to be revised"
            },
            {
                "name": "revision",
                "data_type": "string",
                "placeholder": "Enter code revision",
                "description": "User input for code revision"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "revised_code",
                "data_type": "string",
                "description": "Revised version of the code"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        code = p['code']
        revision = p['revision']

        revised_code = code.replace(code, revision)

        ai_context.set_output('revised_code', revised_code, self)