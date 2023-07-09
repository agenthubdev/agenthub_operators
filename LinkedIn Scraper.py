import requests
from bs4 import BeautifulSoup
from .base_operator import BaseOperator
from ai_context import AiContext

class LinkedInScraperOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'LinkedIn Scraper Operator'

    @staticmethod
    def declare_description():
        return 'This operator scrapes the content from a LinkedIn profile and returns it as a string.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "profile_url",
                "data_type": "string",
                "placeholder": "Enter LinkedIn profile URL",
                "description": "URL of the LinkedIn profile to scrape"
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
                "description": "Scraped LinkedIn profile content"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        profile_url = p['profile_url']
        
        response = requests.get(profile_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_content = soup.get_text()

        ai_context.set_output('output', profile_content, self)