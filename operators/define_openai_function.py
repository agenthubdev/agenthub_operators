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
                    # TODO: Add descriptions
                    {
                        "name": "name",
                        "data_type": "string",
                        "placeholder": "Parameter name (ex: 'location')",
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
        params = step['parameters']
        function_name = params.get('name')
        description = params.get('description')
        # Parameter structures contains parameters in threes
        # Ex. [{'name-0-0': 'location'}, {'type-0-1': 'string'}, {'description-0-2': 'The city and state, e.g. San Francisco, CA.'},
        #      {'name-1-0': 'unit'}, {'type-1-1': 'string'}, {'description-1-2': 'This is the unit of temperature, inferred from the location/city'}]
        parameter_structures = params.get('parameters')

        # Separate individual parameters attributes (segment into 2D array, where each array contains name, type, description)
        # TODO: move this to the platform side to simplify making new operators with object[] parameters
        parameters_dict = self.parse_parameter_structures(parameter_structures)
        # Use the segmented array of parameters to build the function JSON
        self.build_openai_function_json(
            function_name, description, parameters_dict, ai_context)

    def parse_parameter_structures(self, parameter_structures):
        parameters_dict = {}

        for parameter in parameter_structures:
            # Each item is a dictionary with one entry, iterate over this entry
            for attribute, value in parameter.items():
                # Split the key by the "-" character
                # This separates the attribute name (name, type, or description) and the parameter index
                indexed_attribute = attribute.split("-")
                param_index = indexed_attribute[1]
                param_attribute = indexed_attribute[0]

                if param_index not in parameters_dict:
                    parameters_dict[param_index] = {}

                # Add the attribute to the dictionary for this parameter index
                parameters_dict[param_index][param_attribute] = value

        return parameters_dict

    def build_openai_function_json(self, function_name, description, parameters_dict, ai_context):
        # Properties dictionary is what holds the actual parameter information
        properties = {}
        parameter_names = []

        # Iterate over the dictionaries in parameters_dict, which are the dictionaries of parameter attributes
        for parameter in parameters_dict.values():
            # Get each attribute from the parameter dictionary
            parameter_name = parameter["name"]
            parameter_type = parameter["type"]
            parameter_desc = parameter["description"]

            # Add these attributes to the properties dictionary
            properties[parameter_name] = {}
            properties[parameter_name]["type"] = parameter_type
            properties[parameter_name]["description"] = parameter_desc

            # Add the parameter name to the list of parameter names
            parameter_names.append(parameter_name)

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
        ai_context.set_output('function_json', function_json_str, self)
