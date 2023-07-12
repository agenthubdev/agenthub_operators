from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

from .base_operator import BaseOperator
from ai_context import AiContext


import json


class WebSearch(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Web search'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.CONSUME_DATA.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "query",
                "data_type": "string",
                "placeholder": "Enter your search query"
            },
            {
                "name": "results_count",
                "data_type": "integer",
                "placeholder": "Enter the number of results (default 5)"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "urls",
                "data_type": "string[]",
            },
            {
                "name": "snippets",
                "data_type": "string[]"
            }
        ]

    def run_step(self, step, ai_context):
        query = step['parameters'].get('query')
        results_count = step['parameters'].get('results_count')
        if results_count is None:
            results_count = 5
        else:
            results_count = int(results_count)

        google_res = self.google_search(query, results_count, ai_context)
        snippets, urls = self.get_urls_and_snippets(google_res)

        ai_context.add_to_log(
            f'Google results:\n urls={urls}\n snippets={snippets}')

        ai_context.set_output(
            'urls',
            urls,
            self
        )
        ai_context.set_output(
            'snippets',
            snippets,
            self
        )

    def get_urls_and_snippets(self, google_res):
        data = google_res
        titles_and_snippets = []
        links = []
        for item in data.get('items', []):
            titles_and_snippets.append(item['title'] + " " + item['snippet'])
            links.append(item['link'])

        # Snippets are brief descriptions of the website content, similar to the preview on Google Search
        return titles_and_snippets, links

    def google_search(self, query, num_results, ai_context) -> list[str]:
        try:
            custom_search_engine_id = ai_context.get_secret(
                'google_search_engine_id')
            service = build(
                "customsearch", "v1", developerKey=ai_context.get_secret('google_search_developer_key')
            )
            api_response = (
                service.cse()
                .list(q=query, cx=custom_search_engine_id, num=num_results)
                .execute()
            )

            # Extract the search result items (urls and snippets) from the response
            return api_response

        except HttpError as e:
            invalid_api_key_str = 'invalid API key'
            error_details = json.loads(e.content.decode())

            if error_details.get("error", {}).get(
                "code"
            ) == 403 and invalid_api_key_str in error_details.get("error", {}).get(
                "message", ""
            ):
                return f"Error: {invalid_api_key_str}"
            else:
                return f"Error: {e}"
