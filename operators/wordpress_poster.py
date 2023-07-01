from .base_operator import BaseOperator
import json
import requests


class WordpressPoster(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Post to Wordpress'

    @staticmethod
    def declare_description():
        return 'This operator posts content to a Wordpress site.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.ACT.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "wordpress_client_id",
                "data_type": "string",
                "placeholder": "12345",
                "description": "The client ID for your wordpress app at https://developer.wordpress.com/apps/"
            },
            {
                "name": "wordpress_url",
                "data_type": "string",
                "placeholder": "my_name.wordpress.com",
                "description": "URL of the Wordpress site"
            },
            {
                "name": "title",
                "data_type": "string",
                "placeholder": "Cool Post Title",
                "description": "Title of the post"
            },
            {
                "name": "content",
                "data_type": "string",
                "placeholder": "Actual Cool Post Content",
                "description": "Content of the post"
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "title",
                "data_type": "string",
                "placeholder": "Enter post title",
                "description": "Title of the post",
                "optional": "1"
            },
            {
                "name": "content",
                "data_type": "string",
                "placeholder": "Enter post content",
                "description": "Content of the post",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "post_url",
                "data_type": "string",
                "description": "Link to the created post"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']

        wordpress_url = p.get('wordpress_url') or ai_context.get_input(
            'wordpress_url', self)
        title = p.get('title') or ai_context.get_input('title', self)
        content = p.get('content') or ai_context.get_input('content', self)

        access_token = ai_context.get_secret('wordpress_access_token')

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        data = {
            'title': title,
            'content': content,
            'status': 'publish'
        }

        response = requests.post(
            f'https://public-api.wordpress.com/rest/v1.1/sites/{wordpress_url}/posts/new', headers=headers, json=data)

        post_url = response.json().get('URL')
        print(response.json())

        ai_context.set_output('post_url', post_url, self)
        ai_context.add_to_log(f"Post URL: {post_url}")
