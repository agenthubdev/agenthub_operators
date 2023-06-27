from .base_operator import BaseOperator
from ai_context import AiContext


class SaveAsAction(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Save as Action'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DB.value
    
    @staticmethod    
    def declare_parameters():
        return []
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "text",
                "data_type": "string",
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
            {
                "name": "id",
                "data_type": "string",
            }
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        text = ai_context.get_input('text', self)
        run_id = ai_context.get_run_id()
        
        action_id = ai_context.save_as_action(run_id, text)
        ai_context.add_to_log("Saved {} as action {}".format(text, action_id))
        ai_context.set_output('id', action_id, self)
