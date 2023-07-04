import time
import random

from github import Github, GithubException
        
from .base_operator import BaseOperator

from ai_context import AiContext


class GitHubMergeRequester(BaseOperator):
    @staticmethod
    def declare_name():
        return 'Create GitHub merge requests'
    
    @staticmethod
    def declare_category():
        return BaseOperator.OperatorCategory.ACT.value
        
    @staticmethod
    def declare_parameters():
        return [
            {
                "name": "repo_name",
                "data_type": "string",
                "placeholder": "user_name/repository_name"
            },
            {
                "name": "branch",
                "data_type": "string",
                "placeholder": "Enter the branch (default is main)"
            }
        ]
    
    @staticmethod    
    def declare_inputs():
        return [
            {
                "name": "list_of_filenames",
                "data_type": "string[]",
            },
            {
                "name": "list_of_file_contents",
                "data_type": "string[]",
            }
        ]
    
    @staticmethod    
    def declare_outputs():
        return []

    def run_step(
        self, 
        step, 
        ai_context: AiContext
    ):
        params = step['parameters']
        filenames = ai_context.get_input('list_of_filenames', self)
        file_contents = ai_context.get_input('list_of_file_contents', self)

        g = Github(ai_context.get_secret('github_access_token'))
        repo = g.get_repo(params['repo_name'])
        forked_repo = repo.create_fork()

        base_branch_name = params['branch']
        base_branch = repo.get_branch(base_branch_name)

        new_branch_name = f"agent_hub_{ai_context.get_run_id()}"
        GitHubMergeRequester.create_branch_with_backoff(forked_repo, new_branch_name, base_branch.commit.sha)

        run_url = f'https://agenthub.dev/pipeline?run_id={ai_context.get_run_id()}'

        for i in range(len(filenames)):
            file_path = filenames[i]
            new_file_content = file_contents[i]
            
            commit_message = f"{file_path} - commit created by {run_url}"

            try:
                # Attempt to get file
                file = repo.get_contents(file_path, ref=base_branch_name)
                # If file exists, update it
                forked_repo.update_file(file_path, commit_message, new_file_content.encode("utf-8"), file.sha, branch=new_branch_name)
            except GithubException as e:
                if e.status == 404:
                    # If file does not exist, create a new one
                    forked_repo.create_file(file_path, commit_message, new_file_content.encode("utf-8"), branch=new_branch_name)
                else:
                    # If any other error occurred, raise the exception again
                    raise e

        # Create a pull request to merge the new branch in the forked repository into the original branch
        pr_title = f"PR created by {run_url}"
        pr_body = f"PR created by {run_url}"

        pr = repo.create_pull(
            title=pr_title, 
            body=pr_body, 
            base=base_branch_name, 
            head=f"{forked_repo.owner.login}:{new_branch_name}"
        )
        
        ai_context.add_to_log(f"Pull request created: {pr.html_url}")

    @staticmethod  
    def create_branch_with_backoff(forked_repo, new_branch_name, base_branch_sha, max_retries=3, initial_delay=5):
        delay = initial_delay
        retries = 0

        while retries < max_retries:
            try:
                forked_repo.create_git_ref(ref=f"refs/heads/{new_branch_name}", sha=base_branch_sha)
                return
            except Exception as e:
                if retries == max_retries - 1:
                    raise e

                sleep_time = delay * (2 ** retries) + random.uniform(0, 0.1 * delay)
                print(f"Error creating branch. Retrying in {sleep_time:.2f} seconds. Error: {e}")
                time.sleep(sleep_time)
                retries += 1
