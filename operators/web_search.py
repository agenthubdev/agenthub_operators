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
                "name": "search_results",
                # In a bit of hacky way we will store url in 'name' key and snippet in 'content'.
                # So that to make output of this operator immedaitely consumable by ListProcessor.
                # We should think though how detailed should the contract be between operators in terms of 
                # type safety. 
                "data_type": "{name,content}[]",
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
        ai_context.add_to_log(f'Google results:\n urls={urls}\n snippets={snippets}') 
        ai_context.set_output(
            'search_results', 
            [{"name": url, "content": snippet} for url, snippet in zip(urls, snippets)],
            self
        )

        
    def get_urls_and_snippets(self, google_res):
        #data = json.loads(google_res_blob)
        data = google_res
        titles_and_snippets = []
        links = []
        for item in data.get('items', []):
            titles_and_snippets.append(item['title'] + " " + item['snippet'])
            links.append(item['link'])

        return titles_and_snippets, links

    def google_search(self, query, num_results, ai_context) -> list[str]:
        try:
            custom_search_engine_id = ai_context.get_secret('google_search_engine_id')
            service = build(
                "customsearch"
                , "v1"
                , developerKey=ai_context.get_secret('google_search_developer_key')
            )
            api_response = (
                service.cse()
                .list(q=query, cx=custom_search_engine_id, num=num_results)
                .execute()
            )

            # Extract the search result items from the response
            return api_response
            # api_response.get("items", [])

            # Create a list of only the URLs from the search results
            #links = [item["link"] for item in results]

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

        return to_utf8_json_list(links)


def to_utf8_json_list(l) -> str:
    res = json.dumps(
        [s.encode("utf-8", "ignore") for s in l]
    )
    return res
