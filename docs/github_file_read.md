## **GitHubFileReader**

The `GitHubFileReader` class is a custom operator class that inherits from the `BaseOperator` class. It allows the user to fetch files from a GitHub repository and store them as a list of dictionaries containing file names and contents. The class focuses on the functionality of fetching files from a specific GitHub repository using a provided access token, branch, regex filter, and list of folder paths.

**Parameters:**

- `repo_name` (string) : The name of the GitHub repository in the format of "user_name/repository_name".
- `folders` (string) : A list of folder paths separated by commas.
- `file_regex` (string) : A regex pattern to filter file names (e.g., '.*\.py').
- `branch` (string) : The branch of the repository being fetched (default is 'main').

**Outputs:**

- `files` (list of dictionaries) : A list containing dictionaries of fetched files in which each dictionary has the keys 'name' and 'content' set.

**Methods:**

- `declare_name` : Returns the name of the operator, which is 'Get files from GitHub'.
- `declare_category` : Returns the operator category, which is 'CONSUME_DATA'.
- `declare_parameters` : Returns a list of dictionary objects, each containing parameter-related information such as the name, data type, and placeholder.
- `declare_inputs` : Returns an empty list as there are no inputs.
- `declare_outputs` : Returns a list of dictionary objects containing output-related information such as the name and data type.
- `run_step` : Executes the process of fetching files from the specified GitHub repository using the provided parameters.
- `read_github_files` : A helper method that reads files from the GitHub repository using the GitHub API. It leverages a breadth-first search approach to fetch files recursively from parent folders. The fetched files are filtered based on the given regex pattern, and the list of dictionaries containing file names and contents is returned.

The main functionality of the `GitHubFileReader` class is to fetch files from GitHub repositories using the provided access token, branch, regex filter, and folder paths. It connects to the GitHub API and processes the parameters of the step passed to the `run_step` method. Then, it moves on to the `read_github_files` helper function to read file contents and names from specified folders.

After fetching the files from the GitHub repository, the class logs this information, including the number of fetched files and the list of file paths. Finally, the `files` output is set by the `ai_context.set_output()` method.