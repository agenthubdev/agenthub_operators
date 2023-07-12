import requests
import io

from bs4 import BeautifulSoup
import tabula
from PyPDF2 import PdfReader
import pandas as pd

from ai_context import AiContext
from .base_operator import BaseOperator


class WebsiteScraper(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Website Scraper'

    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.CONSUME_DATA.value

    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "url",
                "data_type": "string",
                "placeholder": "Ex. www.bloomberg.com",
                "description": "Enter the URL to scrape the content from. Note: Javascript generated text is not yet supported."
            }
        ]

    @staticmethod
    def declare_inputs():
        return [
            {
                "name": "url",
                "data_type": "string",
                "optional": "1"
            }
        ]

    @staticmethod
    def declare_outputs():
        return [
            {
                "name": "website_content",
                "data_type": "string",
            }
        ]

    def run_step(self, step, ai_context: AiContext):
        params = step['parameters']
        url = params.get(
            'url') or ai_context.get_input('url', self)

        self.ingest(url, ai_context)

    def ingest(self, url, ai_context):
        # TODO: Add Selenium for support of scraping Javascript website
        if url and self.is_url(url):
            if url.lower().endswith(".pdf"):
                file_data = self.load_pdf_from_url(url)
                text = self.read_pdf(file_data)
                ai_context.add_to_log(
                    f"Content from PDF at {url} has been scraped.")
            else:
                text = self.scrape_text(url)
                ai_context.storage['ingested_url'] = url
                ai_context.add_to_log(
                    f"Content from {url} has been scraped.")

            ai_context.set_output('website_content', text, self)
        else:
            ai_context.set_output('website_content', '', self)
            ai_context.add_to_log(
                "Could not find URL or content on website to read.")

    def is_url(self, url):
        # TODO: Add a real is_url check into utils.py
        return True

    def scrape_text(self, url):
        response = requests.get(url)
        bs = BeautifulSoup(response.text, "html.parser")

        for script in bs(["script", "style"]):
            script.extract()

        text = bs.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        text = "\n".join(chunk for chunk in chunks if chunk)

        return text

    def load_pdf_from_url(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response
        return response.content

    def read_pdf(self, pdf):
        pd.set_option('display.max_colwidth', None)
        pdf_content = io.BytesIO(pdf)
        df_list = tabula.read_pdf(pdf_content, pages='all')

        # If tabula returned empty DataFrames, fall back to PyPDF2
        if all(df.empty for df in df_list):
            pdf_reader = PdfReader(pdf_content)
            text = []
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text.append(page.extract_text())
            return "\n".join(text)

        pdf_content = "\n".join(df.to_string(index=False) for df in df_list)
        return pdf_content
