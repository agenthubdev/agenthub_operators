import json

from .base_operator import BaseOperator


class OutputOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Output'

    @staticmethod
    def declare_description():
        return """Special type of operator that is used to (1) create a named output of a pipeline and (2) store output of saved pipeline (e.g. for interacting with Agent in chat mode). Note that history of output values can be stored at different levels of granularity, e.g. for individual user or for a project. 
        """

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "output_name",
                "data_type": "string",
                "description": "Give pipeline output a name",
            },
            {
                "name": "store_log",
                "data_type": "boolean",
                "description": "When making this pipeline an Action of an Agent do you want this output be preserved at all."
            },
            {
                "name": "log_visibility",
                "data_type": "enum(user,project)",
                "description": "When storing the history of outputs for an Agent what level of granularity should the log be stored at.",
                "condition": "store_log == true"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "output",
                "data_type": "any",
            }
        ]

    @staticmethod
    def declare_outputs():
        return []

    def run_step(self, step, ai_context):
        # Does nothing, agenthub.dev platform is implementing special treatment for Input and Output operators.
        pass
