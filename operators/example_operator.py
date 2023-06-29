import re
from .base_operator import BaseOperator
from ai_context import AiContext


class ExampleOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Example Operator'

    @staticmethod
    def declare_description():
        return 'This is an example operator that follows the same structure as the base operator.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "parameter1",
                "data_type": "string",
                "placeholder": "Enter parameter 1",
                "description": "Parameter 1 description"
            },
            {
                "name": "parameter2",
                "data_type": "integer",
                "placeholder": "Enter parameter 2",
                "description": "Parameter 2 description"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "input1",
                "data_type": "string",
                "description": "Input 1 description"
            },
            {
                "name": "input2",
                "data_type": "integer",
                "description": "Input 2 description"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "string",
                "description": "Output description"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        input1 = ai_context.get_input('input1', self)
        input2 = ai_context.get_input('input2', self)
        parameter1 = p['parameter1']
        parameter2 = p['parameter2']

        # Perform some operation using the inputs and parameters
        output = f"Input 1: {input1}, Input 2: {input2}, Parameter 1: {parameter1}, Parameter 2: {parameter2}"
        ai_context.set_output('output', output, self)
