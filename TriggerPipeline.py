import re
from .base_operator import BaseOperator
from ai_context import AiContext

class TriggerPipeline(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Trigger Pipeline'

    @staticmethod
    def declare_description():
        return 'This operator triggers a pipeline using a given input and a saved item id.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "saved item id",
                "data_type": "string",
                "placeholder": "Enter saved item id",
                "description": "The id of the saved item"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "pipeline input",
                "data_type": "string",
                "description": "The input for the pipeline"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "item",
                "data_type": "string",
                "description": "The output item from the function"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        pipeline_input = ai_context.get_input('pipeline input', self)
        saved_item_id = p['saved item id']

        item = ai_context.trigger_pipeline(pipeline_input, saved_item_id)

        ai_context.set_output('item', item, self)