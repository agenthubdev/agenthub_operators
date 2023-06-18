# Scrape Hacker News Operator

## Summary

This operator scrapes and filters Hacker News posts, returning a JSON object containing titles and links of filtered posts.

## Inputs

This operator does not have any inputs.

## Parameters

- `keywords`: A JSON array of keywords that are used to filter news titles (optional).
- `num_pages`: An integer representing the number of pages to scrape (maximum of 5 pages).

## Outputs

- `title_link_dict`: A JSON object containing the titles and links of the filtered posts from Hacker News.

## Functionality

The `run_step` function receives parameters and the AI context, and then calls the `scrape_hacker_news` function with these values.

The `scrape_hacker_news` function retrieves the provided parameters and initializes the `title_link_dict`. It then iterates through the desired number of pages, sending a GET request to the Hacker News URL and parsing the response using Beautiful Soup. For each post, the title and link are extracted, and checks are made to ensure the title contains the specified keywords and does not contain any excluded words. If the title passes these checks, it is added to the `title_link_dict`. 

Finally, the `title_link_dict` is set as the output and a log message is generated to indicate the number of pages that have been scraped and filtered.