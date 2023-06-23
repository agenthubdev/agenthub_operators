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
        output_type = step['parameters'].get('output_type')
        if input_type == "Document[]":
            if output_type == 'string':
                # Document schema from langchain for reference: 
                # https://github.com/hwchase17/langchain/blob/master/langchain/schema.py#L269
                res = " ".join([d.page_content for d in input])
                
                ai_context.set_output('output', res, self)
                return
        elif input_type == 'string':
            if output_type in ['[]', 'string[]']:
                if output_type == '[]':
                    ai_context.set_output('output', [input], self)
                else:
                    ai_context.set_output('output', self.best_effort_string_to_list(input), self)
                return
        elif input_type == 'string[]':
            if output_type == 'string':
                ai_context.set_output('output', ", ".join(input), self)
                return
            

        raise TypeError(f'Dont know how to cast {input_type} to {output_type}')
          
            
    def best_effort_string_to_list(self, s):
        try:
            result = json.loads(s)
            if isinstance(result, dict):
                return [result]  # Wrap the dictionary in a list
            elif isinstance(result, list):
                return result
        except json.JSONDecodeError:
            pass

        result = s.split(',')
        return [item.strip() for item in result]
        

