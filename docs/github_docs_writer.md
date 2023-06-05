# GitHubDocsWriter

The `GitHubDocsWriter` class is a custom operator that focuses on providing **structured documentation** for the code in markdown format. It takes into consideration the comments within the code and offers a summary of the functionality. By digesting the code into an accessible format, the class contributes to an easily comprehended understanding of the code's purpose and operation.

## Key functionalities:

- Declare the **name**, **category**, **parameters**, **inputs**, and **outputs** of the operator.
- *run_step()* method to create a branch, modify files, and create a pull request.
- *create_branch_with_backoff()* helper method to create a branch with exponential backoff in case of errors.

## Parameters:

1. `repo_name`: Repository name in the format `user_name/repository_name`.
2. `docs_folder_name`: Name of the folder where the documentation files will be stored.

## Inputs:

- `code_content`: An array of objects containing the name and content of the code files.

## Outputs:

- No Outputs.

### Purpose of the class:

This class aims to:

1. Create a new branch in a forked version of the input repository.
2. Generate structured documentation in the form of Markdown files for inputted code files, considering comments and providing an explanation of the functionality.
3. Add or update the documentation files in the new branch.
4. Create a pull request to merge the changes in the new branch into the original repository.

### Helper Method's Functionality:

- `create_branch_with_backoff`: This method tries to create a branch with a specified name in the forked repository. In case of errors, it retries the operation with exponential backoff and a random jitter, thus avoiding excessive retries in a short period. The parameters `max_retries` and `initial_delay` allow to fine-tune the backoff behavior if needed.

**Note**: The generated output will be in unrendered markdown format, which allows it to be easily copied into a markdown generator.