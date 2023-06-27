import shortuuid
from enum import Enum

class BaseOperator:
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            self.id = str(shortuuid.uuid())

    def run_step(self, ai_context):
        pass
    
    
    class OperatorCategory(Enum):
        CONSUME_DATA = "Data Intake"
        MANIPULATE_DATA = "Data Manipulation"
        DB = "Database I/O"
        AI = "Using LLMs"
        ACT = "Interact with the World"
        MISC = "The rest"

    # Whether to allow AgentHub platform to execute opreator multiple times in a loop 
    # on a vector inputs. This can be useful when you need to apply operator that is processing
    # a single item to a number of entities in a pipeline.
    @staticmethod
    def declare_allow_batch():
        return False

    # This is user visible operator name that they select on the frontend.   
    @staticmethod
    def declare_name():
        return 'BaseOperator, if you see this it means that derived operator class did not set a proper name.'
        
    # Parameter is something that users need to set manually as part of building pipeline.
    # Note that it is important that we don't confuse 'parameter' vs 'input'.
    @staticmethod
    def declare_parameters():
        return []
        
    # For some operator we want to allow extra configuration that is out of the way de default, e.g.
    # selecting model preference for operators that call LLMs. These would use default value for the
    # pipeline run but occasionally you want to override model preference for one individual operator instance.
    @classmethod
    def declare_additional_parameters(cls):
        if cls.declare_category() == BaseOperator.OperatorCategory.AI.value:
            return [{
                "name": "model_preference",
                "data_type": "enum(gpt-4,gpt-3.5-turbo,gpt-3.5-turbo-16k)",
                "placeholder": ""
            }]
        else:
            return []
        
    # Input state that operator processes, e.g. a list of web links or a blob of text.
    # This is something that user cannot set manually on the UI for now, though later we might 
    # want to enable setting inputs from UI, e.g. for those operators that can be both the first one
    # in a pipeline and also in the middle of a pipeline.
    @staticmethod
    def declare_inputs():
        return []
        
    # See declare_inputs above. One operator's outputs are inputs of another.  
    @staticmethod
    def declare_outputs():
        return []
        
    # Names of secrets subject operator would use.
    @staticmethod
    def declare_secrets():
        return []
    
    # Plain english explanation of what it does, optional.
    @staticmethod
    def declare_description():
        return ""
    
    # Category operator falls into, helps guide operator selection in UI.
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value
