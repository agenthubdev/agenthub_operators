import feedparser
import json
from .base_operator import BaseOperator
from ai_context import AiContext

class RSSToJsonOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'RSS To JSON Operator'

    @staticmethod
    def declare_description():
        return 'This operator reads a URL as an RSS feed and outputs JSON with link and title.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.DATA_PROCESSING.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "url",
                "data_type": "string",
                "placeholder": "Enter RSS feed URL",
                "description": "The URL of the RSS feed to parse"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "output",
                "data_type": "string",
                "description": "The parsed RSS feed in JSON format"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        url = p['url']

        # Parse the RSS feed
        feed = feedparser.parse(url)

        # Extract the link and title from each entry
        output = [{'link': entry.link, 'title': entry.title} for entry in feed.entries]

        # Convert the output to JSON
        output_json = json.dumps(output)

        ai_context.set_output('output', output_json, self)