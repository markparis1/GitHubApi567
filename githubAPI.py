import requests
import json
from typing import Dict

def repositories(id: str):

    repos: [str] = []
    r = requests.get(f"https://api.github.com/users/{id}/repos")

    if not (r.status_code == 200):

        print("Error could not find github id")

    else:

        github_json_repos = r.json()

        for item in github_json_repos:

            for key in item:

                if key == "name":

                    repos.append(item[key])


    
    repos_commits = {}
    for repo in repos:
       
        r = requests.get(f"https://api.github.com/repos/{id}/{repo}/commits")

        if not (r.status_code == 200):

            print("Error could not find github repository")

        else:

            github_json_repos = r.json()
            repos_commits[repo] = len(github_json_repos)
        
    for key in repos_commits:

        print(f"Repo: {key} Number of commits: {repos_commits[key]}")

    



repositories("markparis1")