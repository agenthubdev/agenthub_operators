import re
from .base_operator import BaseOperator
from ai_context import AiContext
from linkedin_scraper import Person, actions
from selenium import webdriver

class LinkedInScraperOperator(BaseOperator):
    @staticmethod
    def declare_name():
        return 'LinkedIn Scraper Operator'

    @staticmethod
    def declare_description():
        return 'This operator scrapes the content of a LinkedIn profile and returns it as a string.'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.MISC.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "linkedin_url",
                "data_type": "string",
                "placeholder": "Enter LinkedIn profile URL",
                "description": "URL of the LinkedIn profile to scrape"
            },
            {
                "name": "email",
                "data_type": "string",
                "placeholder": "Enter your LinkedIn email",
                "description": "Your LinkedIn email for login"
            },
            {
                "name": "password",
                "data_type": "string",
                "placeholder": "Enter your LinkedIn password",
                "description": "Your LinkedIn password for login"
            }
        ]

    @staticmethod
    def declare_inputs():
        return []

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "profile_content",
                "data_type": "string",
                "description": "Content of the scraped LinkedIn profile"
            }
        ]

    def run_step(self, step, ai_context):
        p = step['parameters']
        linkedin_url = p['linkedin_url']
        email = p['email']
        password = p['password']

        driver = webdriver.Chrome()
        driver.get('https://www.linkedin.com')

        actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
        person = Person(linkedin_url, driver=driver)

        profile_content = person.to_string()

        ai_context.set_output('profile_content', profile_content, self)