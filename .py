import re
from .base_operator import BaseOperator
from ai_context import AiContext

class FilterKeywordOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Filter Keyword Operator'

    @staticmethod
    def declare_description():
        return 'This operator filters out items in a list that contain a specific keyword.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "keyword"