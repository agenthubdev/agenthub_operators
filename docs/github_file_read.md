# GitHubFileReader Operator

## Summary

This operator reads and retrieves files from GitHub repositories, considering specified folders, file patterns and branches.

## Inputs

- None, this specific operator doesn't have inputs declared.

## Parameters

- `repo_name`: The full name of the GitHub repository in the format "user_name/repository_name".
- `folders`: Comma-separated list of the folder paths in the repository to search for files.
- `file_regex`: A regular expression pattern to filter which file names should be read. (e.g., '.*\.py')
- `branch`: The branch name to fetch files from (default is 'main').

## Outputs

- `files`: A list of dictionaries, with each dictionary including `name` and `content` keys, representing the file path and file content, respectively.

## Functionality

- The `run_step` method takes a step and an `AiContext` object, and calls the `read_github_files` function with the provided parameters and context.
- The `read_github_files` function initializes the connection with the GitHub API, fetches the files under the specified folders, filter the files based on the given `file_regex`, and stores the files in the `files` list in a dictionary format with `name` and `content` keys.
- The `bfs_fetch_files` function is a helper function to perform Breadth-First Search from a given folder path and fetch the files accordingly. It accesses the files within the specified repository and filters them based on regex filtering if provided.
- Lastly, the operator sets its output as the list of dictionaries with the fetched file names and content.