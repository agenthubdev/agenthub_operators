import re
from .base_operator import BaseOperator
from ai_context import AiContext

class UuidCheckOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Uuid Check Operator'

    @staticmethod
    def declare_description():
        return 'This operator checks if a given string is a uuid.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return []

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "input1",
                "data_type": "string",
                "description": "Input string to check if it's a uuid"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "boolean",
                "description": "Output is true if the input string is a uuid, otherwise false"
            }
        ]

    def run_step(self, step, ai_context):
        input1 = ai_context.get_input('input1', self)

        uuid_regex = re.compile(r'^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)
        match = uuid_regex.match(input1)

        output = bool(match)
        ai_context.set_output('output', output, self)