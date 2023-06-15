# FindBestPost

**FindBestPost** is a class that extends the `BaseOperator`. Its main purpose is to find the best post based on the given query, context string, and available posts. The class processes input and output data and utilizes an AI context instance to perform an AI-related task.

## Inputs

- **title_link_dict**: A dictionary containing the post titles and their corresponding links in JSON format.

## Parameters

- **query**: A user-provided query string.

## Outputs

- **best_post_link**: The link to the best post that matches the user query.

## Functionality 

- `declare_name()`: Returns a string representing the name of the operator, in this case, `Find Best Post`.

- `declare_category()`: Returns the category of the operator, which is the AI category in this instance.

- `declare_parameters()`: Declares the parameters needed for the operator. In this case, it is the query string.

- `declare_inputs()`: Declares the input data, which is a JSON containing the post titles and their corresponding links.

- `declare_outputs()`: Declares the output data, in this case, the link to the best post.

- `run_step(step, ai_context)`: Runs the main logic of the operator on the given step and AI context.

- `find_best_post(params, ai_context)`: Finds and sets the best post based on the given query and AI context. It first filters out used and/or irrelevant links, then creates a context string from the post titles. Next, it constructs a prompt message containing the context string and query, and then runs AI chat completion to select the best post title. Finally, it sets the output as the link associated with the selected title.

The class computes the best post based on the user's query, considering only the unused post links and utilizing the AI context to make a choice. It generates the most relevant post link as the output to meet the user's query criteria.