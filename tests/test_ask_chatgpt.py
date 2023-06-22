from unittest.mock import Mock, patch
import unittest

import sys
from pathlib import Path
# Add the parent directory of this package to PATH so that to 
# make it possible to import other package from here, e.g. util
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from .mock_ai_context import MockAiContext
from .tester import test_operator

class AskChatGptTest(unittest.TestCase):
    def test_ask_chatgpt(self):
        ask_chatgpt_step = {
            "operator": "Ask ChatGPT",
            "parameters" : {
                "question": "What's the weather like today?",
                "max_tokens": 20
            }
        }

        all_tests = [
            {
                'step': ask_chatgpt_step,
                'inputs': {
                    'question': "What's the weather like today?",
                    'context': 'It was sunny today. The user lives in San Francisco.'
                },
                'expected_outputs': {
                    'chatgpt_response': 'Tomorrow will also be sunny.',
                }
            }
        ]

        mock_response = "Tomorrow will also be sunny."
        
        with patch.object(MockAiContext, 'run_chat_completion', return_value=mock_response) as mock_method:
            from operators import AskChatGpt
            test_operator(all_tests, AskChatGpt, self)

        mock_method.assert_called_once_with(prompt='Given the context: [It was sunny today. The user lives in San Francisco.], answer the question or complete the following task: What\'s the weather like today?')
