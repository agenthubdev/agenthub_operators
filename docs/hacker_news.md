# ScrapeHackerNews

**ScrapeHackerNews** is a class that extends `BaseOperator`. It is designed to scrape news from https://news.ycombinator.com/ and filter them based on the provided keywords and number of pages, returning a dictionary containing the title and link of each article.

## Parameters

- `keywords` (optional): A JSON list containing keywords to filter the news articles. Only articles containing at least one keyword in their title will be included in the results.
- `num_pages`: The number of pages to scrape from the website (maximum of 5 pages).

## Inputs

There are no inputs required for this class.

## Outputs

- `title_link_dict`: A JSON dictionary containing the title and link of each filtered news article.

## Functionality

The class contains a single helper method, `scrape_hacker_news`, which takes two parameters: `params` and `ai_context`. This method is responsible for carrying out the actual web scraping and filtering based on the provided parameters.

1. The method first checks whether the provided `num_pages` is within the allowed maximum limit of 5 pages. If not, it logs an error message and returns without processing further.
2. It initializes an empty dictionary `title_link_dict` which will store the filtered news articles.
3. It loops through the specified number of pages, and for each page, sends a request to the corresponding URL.
4. The method uses the BeautifulSoup library to parse the HTML response and extract the news items.
5. Within each news item, it extracts the title and link by selecting the appropriate HTML elements.
6. It filters the news items based on the provided keywords (if any) and a list of excluded words (such as 'AskHN', 'ShowHN', and 'LaunchHN').
7. The filtered news items are added to the `title_link_dict` dictionary with their titles as keys and their links as values.
8. Finally, the `title_link_dict` is set as the output of the class, and a log message is added to indicate the number of pages that have been scraped and filtered.

The **ScrapeHackerNews** class provides an efficient way to scrape and filter news articles from the popular Hacker News website based on user-defined parameters. The resulting output is a JSON dictionary containing the titles and links of the filtered articles, ready for further processing or consumption by other application components.