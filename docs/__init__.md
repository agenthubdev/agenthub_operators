# Documentation

## **AskChatGpt**
The `AskChatGpt` class is used to manage the interaction with OpenAI's GPT-3 model for multi-turn chat-based conversations. It allows you to make requests to the GPT-3 API and generate responses based on a list of messages.

**Inputs:** Message list

**Parameters:** Model name, OpenAI API key, and prompt settings (such as "max tokens" and "temperature")

**Outputs:** Generated response

## **WebSearch**
The `WebSearch` class helps in performing web searches using various search engines. It abstracts the interaction with search engine APIs, making it easier to perform web searches and get search results.

**Inputs:** Search query, search engine, and other optional search parameters

**Parameters:** Search engine API key, and selected search engine (Google, Bing, etc.)

**Outputs:** List of search results

## **GitHubFileReader**
The `GitHubFileReader` class enables you to read files from a specified GitHub repository. It handles the underlying API calls to fetch the file content and returns the file data.

**Inputs:** Repository URL, file path, and branch name (optional)

**Parameters:** GitHub API token

**Outputs:** Content of the specified file

## **GitHubMergeRequester**
The `GitHubMergeRequester` class helps you to create merge requests on GitHub. You can use this class to create a pull request, specifying the source and target branches as well as the description.

**Inputs:** Repository URL, source branch, target branch, title, and description of the merge request

**Parameters:** GitHub API token

**Outputs:** Result of the merge request creation

## **GitHubDocsWriter**
The `GitHubDocsWriter` class is used to update documentation files within a GitHub repository. It allows you to read, update, and commit changes to the specified files in the repository.

**Inputs:** Repository URL, file path, new content, commit message, and branch name (optional)

**Parameters:** GitHub API token

**Outputs:** Result of the file update and commit operation

## **ListProcessor**
The `ListProcessor` class provides a set of helper methods for processing and manipulating lists. It contains useful functions for filtering, sorting, and transforming list data.

**Inputs:** Input list, processing function, and optional parameters

**Outputs:** Processed list

## **IngestData**
The `IngestData` class is used to read and store data from various sources. It can read data from files, databases, APIs, and other external sources.

**Inputs:** Data source, connection parameters, query (if applicable)

**Outputs:** Ingested data

## **IndexData**
The `IndexData` class allows you to index data in Elasticsearch. It abstracts the interaction with the Elasticsearch API, making it easier to index, update, and delete data within an Elasticsearch cluster.

**Inputs:** Data, index name, and optional parameters (e.g., index settings, mappings)

**Outputs:** Result of the indexing operation

## **SplitData**
The `SplitData` class allows you to split data into multiple parts, such as training and testing sets for machine learning purposes.

**Inputs:** Data, ratio, and optional parameters (e.g., random seed, stratification)

**Outputs:** Split data sets

## **IngestPDF**
The `IngestPDF` class enables you to extract text from PDF files.

**Inputs:** PDF file path

**Outputs:** Extracted text

## **IngestDocs**
The `IngestDocs` class is used to read and extract text from different document formats (e.g., Word, PDF).

**Inputs:** Document file path, file format

**Outputs:** Extracted text

## **HybridSearch**
The `HybridSearch` class enables you to perform a search using both full-text search and vector search techniques. It combines the results of both search types and provides a single merged list of results.

**Inputs:** Query, full-text search index, vector index, and optional parameters (e.g., weightings)

**Outputs:** Merged search results

## **Summarize**
The `Summarize` class is used to generate a summarized version of a given text. It utilizes text summarization algorithms to produce a shorter, more concise version of the input text.

**Inputs:** Input text

**Outputs:** Summarized text

## **Tweet**
The `Tweet` class enables you to interact with the Twitter API, allowing you to post tweets, read tweets, and perform other operations on the platform.

**Inputs:** Twitter API credentials, action (tweet, read, etc.), and parameters for the chosen action

**Outputs:** Result of the requested action

## **ScrapeHackerNews**
The `ScrapeHackerNews` class allows you to scrape data from the Hacker News website, such as top posts and comments.

**Inputs:** Target URL, data type (posts or comments)

**Outputs:** Scraped data

## **FindBestPost**
The `FindBestPost` class is used to find the best post from a list, based on specific criteria such as votes, comments, or other metrics.

**Inputs:** Post list, sorting criteria, and optional parameters (e.g., weightings)

**Outputs:** Best post

## **GmailSender**
The `GmailSender` class allows you to send emails using the Gmail API.

**Inputs:** Recipients, subject, body, and optional parameters (e.g., attachments, CC, BCC)

**Parameters:** Gmail API credentials

**Outputs:** Result of the email sending operation

## **PersistVectorIndex**
The `PersistVectorIndex` class helps you store and manage a vector index for similarity search. It provides methods to save the index to disk, load it from disk, and perform similarity searches on the index.

**Inputs:** Vector index, file path (for saving or loading)

**Outputs:** Persisted vector index, search results (for similarity search)

## **CastType**
The `CastType` class provides methods to cast data between different types, such as strings, numbers, and lists.

**Inputs:** Input data, target type

**Outputs:** Converted data

## **ChatBot**
The `ChatBot` class allows you to create and manage a chatbot using conversational AI models.

**Inputs:** Message list, AI model, and optional parameters (e.g., model settings)

**Outputs:** Generated response

## **FullTextSearch**
The `FullTextSearch` class enables you to perform full-text search operations on indexed data. It abstracts the interaction with underlying search engines, allowing you to easily query data and get search results.

**Inputs:** Query, index name, and optional parameters (e.g., filters, sorting)

**Outputs:** Search results

## **CombineStrings**
The `CombineStrings` class is used to concatenate strings from a list of strings, optionally with a separator.

**Inputs:** List of strings, separator (optional)

**Outputs:** Combined string

## **InputOperator**
The `InputOperator` class is a utility class providing methods to handle user input, such as text input and file uploads.

**Inputs:** Input type, prompt, and optional validation function

**Outputs:** User input

## **VectorizeOperator**
The `VectorizeOperator` class enables you to convert text into vectors using pre-trained word embeddings or other vectorization techniques.

**Inputs:** Text data, vectorization method, and optional parameters (e.g., pre-trained model)

**Outputs:** Vectorized data