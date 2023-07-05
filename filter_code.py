import re
from .base_operator import BaseOperator
from ai_context import AiContext

class FilterOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Filter Operator'
    
    @staticmethod
    def declare_description():
        return 'This operator filters out items in a list of strings that contain a keyword.'
    
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
                "description": "The keyword to filter the list"
            }
        ]
    
    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "input_list",
                "data_type": "list",
                "description": "The list of strings to filter"
            }
        ]
    
    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "filtered_list",
                "data_type": "list",
                "description": "The filtered list of strings"
            }
        ]
    
    def run_step(self, step, ai_context):
        p = step['parameters']
        input_list = ai_context.get_input('input_list', self)
        keyword = p['keyword']
        
        filtered_list = [item for item in input_list if keyword not in item]
        
        ai_context.set_output('filtered_list', filtered_list, self)