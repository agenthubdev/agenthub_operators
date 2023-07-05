import re
from .base_operator import BaseOperator
from ai_context import AiContext

class FilterKeywordOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Filter Keyword Operator'

    @staticmethod
    def declare_description():
        return 'This operator filters out items in a list that contain a specific keyword.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "keyword",
                "data_type": "string",
                "placeholder": "Enter keyword",
                "description": "Keyword to filter out from the list"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "input_list",
                "data_type": "list",
                "description": "List of strings to filter"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output_list",
                "data_type": "list",
                "description": "Filtered list of strings"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        input_list = ai_context.get_input('input_list', self)
        keyword = p['keyword']

        # Filter out items that contain the keyword
        output_list = [item for item in input_list if keyword not in item]

        ai_context.set_output('output_list', output_list, self)