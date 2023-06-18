# GitHub Docs Writer

## Summary

The GitHub Docs Writer operator automatically generates documentation in markdown format for a given code, and creates a pull request in a specified GitHub repository.

## Inputs

- `code_content`: A list of dictionaries with the following keys:
  - `name`: The file path of the code file
  - `content`: The content of the code file to generate documentation

## Parameters

- `repo_name`: The full name of the GitHub repository to create a pull request in, in the format "user_name/repository_name".
- `docs_folder_name`: The name of the folder in the repository where the generated documentation files should be placed.

## Outputs

There are no defined outputs for this operator.

## Functionality

The `run_step` function performs the following actions:

1. Retrieves the specified repository and creates a fork.

2. Retrieves the base branch ("main" by default) and creates a new branch in the forked repository with a unique name based on the Agent Hub run ID.

3. Iterates through the provided code files in the `code_content` input:
   - For each code file, generates a markdown documentation file using the given content.
   - If the markdown file already exists in the original repository, updates the file in the new branch of the forked repository.
   - If the markdown file does not exist, creates a new file in the new branch of the forked repository.

4. Creates a pull request in the original repository to merge the new branch from the forked repository.

Additionally, there is a helper function `create_branch_with_backoff` that handles branch creation with retries and backoff in case of failure.

The generated pull request contains the markdown documentation for the supplied code content.