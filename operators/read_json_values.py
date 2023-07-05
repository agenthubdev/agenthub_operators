import json

from .base_operator import BaseOperator
from ai_context import AiContext

class ReadJsonValues(BaseOperator):
    @staticmethod
    def declare_name():
        return 'ReadJsonValues'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MANIPULATE_DATA.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "keys",
                "data_type": "string",
                "placeholder": "Ex: 'key1,key2,key3'"
            }
        ]
    
    @staticmethod
    def declare_allow_batch():
        return True

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "json_string",
                "data_type": "string",
                "placeholder": "Enter the JSON string"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "json_values",
                "data_type": "string",
            }
        ]

    def get_nested_values(self, json_object, keys):
        values = []

        for key in keys:
            # If key is nested
            if '.' in key:
                nested_keys = key.split('.')
                temp_json_object = json_object

                # Traverse the json object using the nested keys
                for nested_key in nested_keys:
                    if nested_key in temp_json_object:
                        temp_json_object = temp_json_object[nested_key]
                
                # Add the final value to the list
                values.append(temp_json_object)
            
            # If key is not nested
            elif key in json_object:
                values.append(json_object[key])

        return values

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        json_string = ai_context.get_input('json_string', self)
        params = step['parameters']
        keys = params.get('keys').split(',')

        try:
            json_object = json.loads(json_string)

            values = self.get_nested_values(json_object, keys)
            
            json_values = ', '.join(values)

            ai_context.add_to_log(f"Json values read: {json_values}")
            ai_context.set_output('json_values', json_values, self)

        except Exception as e:
            ai_context.add_to_log(f"Failed to read JSON values. Error: {e}", color='red')
