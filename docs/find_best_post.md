## Summary

This operator finds the best post based on a given query by processing a given list of post titles and links and returning the most relevant post's link.

## Inputs

* `title_link_dict`: A JSON object containing post titles and their corresponding links.

## Parameters

* `query`: A string representing the user's query that will be used to find the most relevant post.

## Outputs

* `best_post_link`: A string containing the most relevant post's link.

## Functionality

* `run_step(self, step, ai_context: AiContext)`: This method calls the `find_best_post()` method with the parameters and AI context.
* `find_best_post(self, params, ai_context)`: This method finds the most relevant post to a given query. It first removes already used links, then creates a context string with the remaining titles. Then, it constructs a prompt message and gets the best post title using chat completion. Finally, it extracts the link of the best post title and sets the output.

The main functionality of this operator is achieved by using the chat completion feature to analyze the provided post titles and select the one that best matches the user's query.