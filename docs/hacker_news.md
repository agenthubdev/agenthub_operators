## ScrapeHackerNews

The **ScrapeHackerNews** class is a part of a web scraping program that retrieves news articles from the '*Hacker News*' website. The class filters the scraped data based on provided **keywords** and a specific number of **pages** (limited to 5 pages). To avoid irrelevant articles, it does not include news with specific excluded words like 'AskHN', 'ShowHN', 'LaunchHN', etc.

The class consists of some essential helper methods to perform the task:

- `declare_name()`: Returns the name of the operator, 'Scrape Hacker News'.
- `declare_category()`: Returns the operator's category, which is 'CONSUME_DATA'.
- `declare_parameters()`: Contains the parameters required for the operation, including **keywords** (list of words used for filtering) and the number of **pages** to scrape (integer, max 5 pages).
- `declare_inputs()`: Returns an empty list as there are no inputs required for this operator.
- `declare_outputs()`: Returns output information, which is a JSON object containing the titles and links of filtered news articles.
- `run_step()`: Executes the web scraping operation based on the given parameters (keywords and num_pages) and AiContext (ai_context).
- `scrape_hacker_news()`: The main logic for iterating through the provided pages, filtering by the given keywords and avoiding specific excluded words.

By using this class, you can effectively filter and retrieve news articles from the '*Hacker News*' website based on your interests and requirements.