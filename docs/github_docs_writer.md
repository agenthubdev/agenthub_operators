# GitHubDocsWriter

**GitHubDocsWriter** is a class that inherits from the `BaseOperator`. This class is responsible for creating and updating markdown files in a specified repository folder with provided content. It forks the target repository, makes changes in the fork, and then creates a pull request to merge the changes back into the original repository.

## Inputs, Parameters, and Outputs

- **Inputs:** 
  - `code_content`: It is of data type `[{name,content}[]]` which contains the input code content as well as the file name.

- **Parameters:**
  - `repo_name`: The GitHub repository in the format `"user_name/repository_name"`
  - `docs_folder_name`: The folder in the repository where the markdown files will be created or updated.

- **Outputs:** The class does not return any output.

## Functionality

1. **declare_name:** This static method returns the name of the class, `'GitHub Docs Writer'`.

2. **declare_category:** This static method returns the operator category, which is `'ACT'`.

3. **declare_parameters:** This static method returns the metadata for the required parameters (`repo_name` and `docs_folder_name`).

4. **declare_inputs:** This static method returns the metadata for the required inputs (`code_content`).

5. **declare_outputs:** This static method returns an empty list as there are no outputs.

6. **run_step:** This method is the main function that:
    - Connects to the GitHub API using the user's access token.
    - Forks the specified repository.
    - Creates a new branch in the forked repository.
    - Loops through the given code content and creates or updates the respective markdown files in the specified docs folder.
    - Creates a pull request with the changes for the original repository.

7. **create_branch_with_backoff:** This static helper method tries to create a branch in the forked repo. If an exception occurs, it retries the process with an increasing delay (with a maximum of `max_retries` retries).

The resulting markdown files from this class can be directly used for documentation purposes, and the output in unrendered markdown format can be copied into a markdown generator for further editing and rendering.