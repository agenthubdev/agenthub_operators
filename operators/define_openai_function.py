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
                "name": "parameters",
                "data_type": "object[]",
                "structure": [
                    {
                        "name": "name",
                        "data_type": "string",
                        "description": "Parameter name (ex: 'location')",
                    },
                    {
                        "name": "type",
                        "data_type": "string",
                        "placeholder": "Parameter type (ex: 'string')",
                    },
                    {
                        "name": "description",
                        "data_type": "string",
                        "placeholder": "Parameter description (ex: 'The city and state, e.g. San Francisco, CA')",
                    }
                ]
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
        function_name = step['parameters'].get('name')
        description = step['parameters'].get('description')
        # Parameter structures contains parameters in threes
        # Ex. first three elements of parameter_structures would be the name, type, and description for one parameter
        parameter_structures = step['parameters'].get('parameters')

        # Separate individual parameters attributes (segment into 2D array, where each array contains name, type, description)
        parameters = [parameter_structures[i:i + 3]
                      for i in range(0, len(parameter_structures), 3)]

        # Properties dictionary is what holds the actual parameter information
        properties = {}

        parameter_names = []

        for parameter in parameters:
            parameter_name = parameter[0]
            parameter_type = parameter[1]
            parameter_desc = parameter[2]

            for _, name in parameter_name.items():
                properties[name] = {}
                parameter_names.append(name)

            for _, type in parameter_type.items():
                properties[name]["type"] = type

            for _, desc in parameter_desc.items():
                properties[name]["description"] = desc

        function_json = {}

        function_json["name"] = function_name
        function_json["description"] = description

        function_json["parameters"] = {}
        function_json["parameters"]["type"] = "object"
        function_json["parameters"]["properties"] = properties
        # By default all parameters will be required
        function_json["parameters"]["required"] = parameter_names

        function_json_str = json.dumps(function_json)
        ai_context.add_to_log(f"Your function json: {function_json_str}")
        ai_context.set_output(
            'function_json', function_json_str, self)
