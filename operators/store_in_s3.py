import os
import json
import boto3
import requests
from urllib.parse import urlparse
from botocore.exceptions import ClientError

from .base_operator import BaseOperator

from ai_context import AiContext


class StoreInS3(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Store in S3'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DB.value
    
    @staticmethod    
    def declare_parameters():
        return [
            {
                "name": "file_name",
                "data_type": "string",
                "placeholder": "File name (object key) that will be stored in S3",
            },
            {
                "name": "s3_bucket",
                "data_type": "string",
                "placeholder": "S3 bucket name",
            },            
            {
                "name": "overwrite",
                "data_type": "boolean"
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "file_url",
                "data_type": "string"
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return [
            {
                "name": "s3_file_uri",
                "data_type": "string",
            }            
        ]

    @staticmethod
    def get_default_file_name(file_url):
        # Parse the URL into its components
        path = urlparse(file_url).path
        path_parts = os.path.split(path)

        # Get the file name (the last part of the path)
        file_name_with_extension = path_parts[-1]

        # Split the file name into its name and extension
        file_name, ext = os.path.splitext(file_name_with_extension)
        return file_name

    @staticmethod
    def upload_to_s3(file_url, file_name, overwrite, s3_bucket, aws_credentials):
        response = requests.get(file_url)

        s3 = boto3.client('s3', 
                        aws_access_key_id=aws_credentials['aws_access_key_id'], 
                        aws_secret_access_key=aws_credentials['aws_secret_access_key'], 
                        region_name=aws_credentials['aws_region_name'])

        try:
            s3.head_object(Bucket=s3_bucket, Key=file_name)
            # If an exception is raised, the object exists
            if not overwrite:
                raise ValueError('Object already exists and overwrite is set to False')
        except ClientError:
            # If the object does not exist, head_object will raise a ClientError
            pass

        # Put object overwrites an existing object by default
        s3.put_object(Body=response.content, Bucket=s3_bucket, Key=file_name)

        # Return the S3 uri
        return f"s3://{s3_bucket}/{file_name}"

    def run_step(
        self,
        step,
        ai_context: AiContext
    ):
        # Get AWS credentials
        aws_credentials = json.loads(ai_context.get_secret('aws_credentials'))

        # Parse inputs
        file_url = ai_context.get_input('file_url', self)

        # Parse parameters
        p = step['parameters']

        s3_bucket = p['s3_bucket']
        overwrite = p.get('overwrite', False)
        file_name = p.get('file_name')
        if not file_name:
            file_name = StoreInS3.get_default_file_name(file_url)

        # Validation
        if any(not value for value in aws_credentials.values()) or not s3_bucket:
            raise ValueError('All AWS credentials and S3 bucket must be provided')

        # Upload file to S3 and set output
        s3_file_uri = StoreInS3.upload_to_s3(file_url, file_name, overwrite, s3_bucket, aws_credentials)

        ai_context.set_output('s3_file_uri', s3_file_uri, self)
        ai_context.add_to_log(f'Successfully saved file at {s3_file_uri}!')