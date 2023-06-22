import sys
from pathlib import Path
# Add the parent directory of this package to PATH so that to 
# make it possible to import other package from here, e.g. util
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from unittest.mock import Mock, patch
import unittest

from .mock_ai_context import MockAiContext
from .tester import test_operator

class CombineStringsTest(unittest.TestCase):
    def test_combine_strings(self):
        combine_strings_step = {
            "operator": "CombineStrings",
            "parameters" : {
                "format": "This is input 1: {input1} This is input 2: {input2}"
            }
        }

        all_tests = [
            {
                'step': combine_strings_step,
                'inputs': {
                    'input1': 'Hello',
                    'input2': 'World'
                },
                'expected_outputs': {
                    'combined_string': 'This is input 1: Hello This is input 2: World',
                }
            },
            {
                'step': combine_strings_step,
                'inputs': {
                    'input1': 'Morning',
                    'input2': 'Sunshine'
                },
                'expected_outputs': {
                    'combined_string': 'This is input 1: Morning This is input 2: Sunshine',
                }
            },
            {
                'step': combine_strings_step,
                'inputs': {
                    'input1': '',
                    'input2': ''
                },
                'expected_outputs': {
                    'combined_string': 'This is input 1:  This is input 2: ',
                }
            }
        ]

        from operators import CombineStrings
        test_operator(all_tests, CombineStrings, self)
