import sys
from pathlib import Path
# Add the parent directory of this package to PATH so that to 
# make it possible to import other package from here, e.g. util
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from unittest.mock import Mock, patch
import unittest

from .mock_ai_context import MockAiContext

from .tester import test_operator

class EncodeURLTest(unittest.TestCase):
    def test_encode_url(self):
        encode_url_step = {
            "operator": "EncodeURL",
        }

        all_tests = [
            {
                'step': encode_url_step,
                'inputs': {
                    'input': 'https://www.example.com/test?param1=hello&param2=world'
                },
                'expected_outputs': {
                    'encoded_url': 'https%3A%2F%2Fwww.example.com%2Ftest%3Fparam1%3Dhello%26param2%3Dworld',
                }
            },
            {
                'step': encode_url_step,
                'inputs': {
                    'input': 'Hello World!'
                },
                'expected_outputs': {
                    'encoded_url': 'Hello+World%21',
                }
            },
            {
                'step': encode_url_step,
                'inputs': {
                    'input': 'Special characters: @#&=+$,'
                },
                'expected_outputs': {
                    'encoded_url': 'Special+characters%3A+%40%23%26%3D%2B%24%2C',
                }
            }
        ]
        
        with patch('ai_context.AiContext', new=MockAiContext):
            from operators import EncodeURL
            test_operator(all_tests, EncodeURL, self)
