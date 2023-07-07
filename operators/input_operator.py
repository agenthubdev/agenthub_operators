import json

from .base_operator import BaseOperator


class InputOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Input'

    @staticmethod
    def declare_description():
        return """Special type of operator that is used to (1) create a named input for a pipeline and 
        (2) to store history of interactions with pipeline when it implements action of an Agent.
        When testing you can specify 'value' parameter manually for Input operator.
        """

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "value",
                "data_type": "string",
                "description": "string value you would like this operator instance to output"
            },
            {
                "name": "input_name",
                "data_type": "string",
                "description": "Named input for the pipeline, can be used to invoke the pipeline with specified input values.",
            },
            {
                "name": "show_as_user_input",
                "data_type": "boolean",
                "description": "Do you want to prompt the end user to fill this field.",
            },
            {
                "name": "input_type",
                "data_type": "enum(text,number)",
                "description": "Type of the input value.",
                "condition": "show_as_user_input == true"
            },
            {
                "name": "store_log",
                "data_type": "boolean",
                "description": "Whether you want to keep track of all the inputs that this pipeline was run with. Makes more sense when building interactive agents and less so for one off experiments."
            },
            {
                "name": "log_visibility",
                "data_type": "enum(user,project)",
                "description": "When storing the history of inputs for this saved pipeline what level of granularity should the log be stored at.",
                "condition": "store_log == true"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        ai_context.set_output('output', p['value'], self)
