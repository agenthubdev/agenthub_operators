import json

from .base_operator import BaseOperator
from ai_context import AiContext


class DefineOpenAiFunction(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Define OpenAi Function'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MANIPULATE_DATA.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "name",
                "data_type": "string",
                "placeholder": "Name your function (ex: 'get_user_details')"
            },
            {
                "name": "description",
                "data_type": "string",
                "placeholder": "Describe your function's purpose for the model to understand"
            },
            {
                "name": "function_body",
                "data_type": "string",
                "placeholder": "Provide a valid json to denote your function params"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "function_json",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        name = step['parameters'].get('name')
        description = step['parameters'].get('description')
        function_body = step['parameters'].get('function_body')

        try:
            function_body_dict = json.loads(function_body)
            function_dict = {
                "name": name,
                "description": description,
                "parameters": function_body_dict,
            }

            function_json = json.dumps(function_dict)
            ai_context.add_to_log(f"Your function json: {function_json}")
            ai_context.set_output('function_json', function_json, self)
        except json.JSONDecodeError as e:
            ai_context.add_to_log(f"Failed to parse function body or create valid JSON. Error: {str(e)}", color='red')
            