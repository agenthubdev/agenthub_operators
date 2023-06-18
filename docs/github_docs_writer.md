# GitHubDocsWriter

The `GitHubDocsWriter` is a class that allows the user to update documentation files on a GitHub repository. It extends the `BaseOperator` class and implements the `run_step()` method.

## Inputs
The `run_step()` method requires one input, `code_content`, which is a list of dictionaries containing the name and content of code files.

## Parameters
The `GitHubDocsWriter` class has two required parameters:

* `repo_name`: the name of the GitHub repository in the format `user_name/repository_name`.
* `docs_folder_name`: the name of the folder in the repository where the documentation files will be stored.

## Outputs
The `run_step()` method does not return any output.

## Methodology

The `run_step()` method follows these steps:

1. Get the values from the input and parameters.
2. Create a fork of the original repository using the GitHub API.
3. Get the base branch of the original repository and the list of all the files in the repository.
4. Create a new branch with a name related to the current run_id.
5. Create and update the documentation files in the forked repository.
6. Create a pull request to merge the changes into the base branch.

The `create_branch_with_backoff()` method is a helper method used to create a new branch in the forked repository. It retries the creation of the branch up to three times with an exponential backoff strategy in case of failure.

Overall, the `GitHubDocsWriter` class is an efficient way to update and manage documentation files in a GitHub repository with the use of Python.