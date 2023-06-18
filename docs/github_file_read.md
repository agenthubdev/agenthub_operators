# **GitHubFileReader**

This class is designed to fetch files from a GitHub repository. It takes four parameters: repository name, folders to fetch files from, file regex to filter the files and the branch to select.

The function `run_step` reads in the user-defined parameters and calls the `read_github_files` function. Inside the `read_github_files` function, the `Github` module authenticates the user using an access token and fetches the required repository. Then the function `bfs_fetch_files` performs a breadth-first search through the folders provided, fetching all files and directories. The files are then filtered based on the provided regex and the decoded content is stored in a list of dictionary objects with keys `name` and `content`.

The function `file_matches_regex` matches the file path against the file regex. If no regex is provided, it returns true. The function `bfs_fetch_files` fetches the files from the repository using a breadth-first search. It fetches all files and directories in the given path, and if a file matches the regex, it is added to the list `files`. If a directory is found, it is added to the queue to process its contents.

The inputs for this class include none, as it is designed to fetch data from the external repository. The parameters are `repo_name`, `folders`, `file_regex`, and `branch` which allow the user to fetch files from the specified repository. The `files` are the only output, which is a list of dictionaries containing the name and content of each file.

In summary, this class fetches multiple files with the specified regex from a specified repository on GitHub and outputs those files as a list of dictionary objects.