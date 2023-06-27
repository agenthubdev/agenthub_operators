from .base_operator import BaseOperator
from ai_context import AiContext


class LoadAction(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Load Action'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DB.value
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "action_id",
                "data_type": "string",
                "placeholder": "Enter the id of your stored action (or pass it as input))",
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "action_id",
                "data_type": "string",
                "optional": "1"

            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
            {
                "name": "action_data",
                "data_type": "string",
            }
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        params = step['parameters']
        action_id_input = ai_context.get_input('action_id', self)
        action_id_param = params.get('action_id')

        # If action_id_input is present, it takes precedence over action_id_param
        action_id = action_id_input if action_id_input is not None else action_id_param

        action_data = ai_context.retrieve_action(action_id)
        ai_context.add_to_log("Loaded action {} with data {}".format(action_id, action_data))
        ai_context.set_output('action_data', action_data, self)
