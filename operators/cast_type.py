import json

from .base_operator import BaseOperator

from ai_context import AiContext


class CastType(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Cast Type'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MANIPULATE_DATA.value
   
    @staticmethod     
    def declare_parameters():
        return [
            {
                "name": "output_type",
                "data_type": "enum(string,string[])",
                "placeholder": "Output type to cast to."
            },
            {
                "name": "is_comma_separated",
                "data_type": "boolean",
                "description": "Do you want to split the input string by commas?",
                "condition": "output_type == string[]"
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "input",
                "data_type": "any",
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "any",
            }
        ]

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        input = ai_context.get_input('input', self)  # >_<
        input_type = ai_context.get_input_type('input', self)
        params = step['parameters']
        output_type = params.get('output_type')
        is_comma_separated = params.get('is_comma_separated', 'false').lower() == 'true'
        if input_type == "Document[]":
            if output_type == 'string':
                # Document schema from langchain for reference: 
                # https://github.com/hwchase17/langchain/blob/master/langchain/schema.py#L269
                res = " ".join([d.page_content for d in input])
                
                ai_context.set_output('output', res, self)
                return
        elif input_type == 'string':
            if output_type in ['[]', 'string[]']:
                ai_context.set_output('output', self.best_effort_string_to_list(input, is_comma_separated), self)
                return
        elif input_type == 'string[]':
            if output_type == 'string':
                ai_context.set_output('output', ','.join(input), self)
                return

        raise TypeError(f'Dont know how to cast {input_type} to {output_type}')
          
            
    def best_effort_string_to_list(self, s, is_comma_separated):
        try:
            result = json.loads(s)
            if isinstance(result, dict):
                return [result]  # Wrap the dictionary in a list
            elif isinstance(result, list):
                return result
        except json.JSONDecodeError:
            pass
        
        if not is_comma_separated:
            return [s]

        result = s.split(',')
        return [item.strip() for item in result]