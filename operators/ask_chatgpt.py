import json

from .base_operator import BaseOperator


class AskChatGpt(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Ask ChatGPT'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.AI.value
        
    @staticmethod
    def declare_allow_batch():
        return True
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "question",
                "data_type": "string",
                "placeholder": "Enter your question"
            },
            {
                "name": "context",
                "data_type": "string",
                "placeholder": "Enter context (optional)"
            },
            {
                "name": "max_tokens",
                "data_type": "integer",
                "placeholder": "Enter max tokens for response"
            }
        ]
     
    @staticmethod   
    def declare_inputs():
        return [
            {
                "name": "question",
                "data_type": "string",
                "optional": "1"
            },
            {
                "name": "context",
                "data_type": "string",
                "optional": "1"
            },
            {
                "name": "function",
                "data_type": "string",
                "optional": "1"
            },
            
        ]
    
    @staticmethod 
    def declare_outputs():
        return [
            {
                "name": "chatgpt_response",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        question = p.get('question') or ai_context.get_input('question', self)
        # We want to take context both from parameter and input.
        input_context = ai_context.get_input('context', self)
        parameter_context = p.get('context')

        #Currently only supports one function as input. Will refactor once multiple inputs are supported for operators.
        function = ai_context.get_input('function', self)
        
        context = ''
        if input_context:
            context += f'[{input_context}]'
        
        if parameter_context:
            context += f'[{parameter_context}]'

        if context:
            question = f'Given the context: {context}, answer the question or complete the following task: {question}'
            
        if function:
            functions = [json.loads(function)] if function else None
            ai_response = ai_context.run_chat_completion(prompt=question, functions=functions)
        
        else:
            ai_response = ai_context.run_chat_completion(prompt=question)
        
        # Convert the AI response to string.
        ai_response = str(ai_response)

        ai_context.set_output('chatgpt_response', ai_response, self)
        ai_context.add_to_log(f'Response from ChatGPT: {ai_response}', save=True)
