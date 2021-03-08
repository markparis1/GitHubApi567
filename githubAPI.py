import requests
import json

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
        return repos
print(repositories("markparis1"))