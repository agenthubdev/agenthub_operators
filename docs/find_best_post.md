# FindBestPost

This class extends `BaseOperator` and declares the necessary inputs, parameters, and outputs to find the best post based on a user query. 

The `declare_parameters` method declares the `query` parameter, which is a string input that takes a user's query. The `declare_inputs` method declares the `title_link_dict` input, which is a dictionary of post titles and their corresponding links. The `declare_outputs` method declares the `best_post_link` output, which is a string output that returns the link to the best post.

The `run_step` method receives the step dictionary and `ai_context`. It extracts the parameters and calls the `find_best_post` method.

The `find_best_post` method extracts the query, input title links, and any previously used links. It filters out the previously used links and converts the remaining title links into a context string. It then generates a message prompt to request the user to select the best post title that fits their query. Once the prompt message is generated, it calls the `run_chat_completion` method with the prompt message to get the user's input response. It then checks whether the user's input response matches any of the remaining titles and returns the best match, along with its corresponding link.

The `add_to_log` method is a helper method that adds a log message entry to the ai_context.

Overall, this class aims to find the most relevant post to a user's query and return the link to the best post.