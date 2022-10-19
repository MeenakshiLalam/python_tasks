
import requests

username="MeenakshiLalam"
url=f"https://api.github.com/users/{username}"
projects=requests.get(url).json()
print(projects)
import base64
from github import Github
username="MeenakshiLalam"
g=Github()
user=g.get_user(username)
for repo in user.get_repos():
    print(repo)

    
    
    
 OUTPUT:
  Repository(full_name="MeenakshiLalam/eks-demos")
Repository(full_name="MeenakshiLalam/hello_from_git")
Repository(full_name="MeenakshiLalam/mohan")
Repository(full_name="MeenakshiLalam/python-assignments")
Repository(full_name="MeenakshiLalam/python_tasks")
