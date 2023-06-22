from unittest.mock import Mock, patch
import unittest

import sys
from pathlib import Path
# Add the parent directory of this package to PATH so that to 
# make it possible to import other package from here, e.g. util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from botocore.exceptions import ClientError

from .mock_ai_context import MockAiContext
from .tester import test_operator

class StoreInS3Test(unittest.TestCase):
    def test_store_in_s3(self):
        # Mock the content that will be returned when the requests.get method is called
        mock_response = Mock()
        mock_response.content = b"file content"

        # Mock the boto3 S3 client's methods
        mock_s3 = Mock()
        # Simulates a non-existing object
        mock_s3.head_object.side_effect = ClientError(
            {"Error": {"Code": "404", "Message": "Not Found"}}, "head_object"
        )
        # Simulates successful upload
        mock_s3.put_object.return_value = None

        store_in_s3_step = {
            "operator": "Store in S3",
            "parameters" : {
                "file_name": "my_file.pdf",
                "s3_bucket": "my_bucket",
                "overwrite": False
            }
        }

        all_tests = [
            {
                'step': store_in_s3_step,
                'inputs': {
                    'file_url': 'http://mockurl.com/my_file.pdf',
                },
                'expected_outputs': {
                    's3_file_uri': 's3://my_bucket/my_file.pdf',
                }
            }
        ]
        
        with patch('requests.get', return_value=mock_response), patch('boto3.client', return_value=mock_s3):
            from operators import StoreInS3
            test_operator(all_tests, StoreInS3, self)
