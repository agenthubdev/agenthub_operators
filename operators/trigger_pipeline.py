from ai_context import AiContext
from .base_operator import BaseOperator


class TriggerPipeline(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Trigger Pipeline'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.CONSUME_DATA.value

    @staticmethod
    def declare_description():
        return "Triggers another pipeline with provided input and returns its output"

    @staticmethod
    def declare_allow_batch():
        return True

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "saved_item_id",
                "data_type": "string",
                "placeholder": "Ex: 14320843921804932",
                "description": "Enter the ID of the saved item"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "pipeline_input",
                "data_type": "string",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        params = step['parameters']
        saved_item_id = params.get('saved_item_id')
        pipeline_input = ai_context.get_input('pipeline_input', self) or ''

        self.trigger(saved_item_id, pipeline_input, ai_context)

    def trigger(self, saved_item_id, pipeline_input, ai_context):
        if saved_item_id:
            ai_context.add_to_log(
                f"Triggering pipeline with saved item id {saved_item_id}.")

            output = ai_context.trigger_pipeline(saved_item_id, pipeline_input)

            ai_context.set_output('output', output, self)
            
            ai_context.add_to_log(
                f"Pipeline with saved item id {saved_item_id} has been triggered.")
        else:
            ai_context.set_output('output', '', self)
            ai_context.add_to_log("No saved item id to trigger pipeline.")
