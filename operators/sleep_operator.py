import time

from .base_operator import BaseOperator


class SleepOperator(BaseOperator):
    @staticmethod
    def declare_visibility():
        return [('project', '<insert agenthub project id>')]

    @staticmethod
    def declare_description():
        return 'Just sleeps and does nothing useful, we are mostly adding it for testing purposes.'

    @staticmethod
    def declare_name():
        return 'Sleep Operator'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "sleep_seconds",
                "data_type": "string",
                "placeholder": "How many seconds to sleep for"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return []

    def run_step(self, step, ai_context):
        p = step['parameters']
        s = float(p['sleep_seconds'])
        time.sleep(s)
