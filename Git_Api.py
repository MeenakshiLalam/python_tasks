import requests
response = requests.get("https://api.github.com/users/MeenakshiLalam/repos")
username="MeenakshiLalam"
url=f"https://api.github.com/users/{username}"
my_projects = response.json()
print("list of Github urls")
for projects in my_projects:
    print( projects['url'])

print("list of repository names")

import base64
from github import Github
username="MeenakshiLalam"
g=Github()
user=g.get_user(username)
for repo in user.get_repos():
    print(repo)


 


    
    
    
 OUTPUT:
    
list of Github urls
https://api.github.com/repos/MeenakshiLalam/eks-demos
https://api.github.com/repos/MeenakshiLalam/hello_from_git
https://api.github.com/repos/MeenakshiLalam/mohan
https://api.github.com/repos/MeenakshiLalam/python-assignments
https://api.github.com/repos/MeenakshiLalam/python_tasks

list of repository names
Repository(full_name="MeenakshiLalam/eks-demos")
Repository(full_name="MeenakshiLalam/hello_from_git")
Repository(full_name="MeenakshiLalam/mohan")
Repository(full_name="MeenakshiLalam/python-assignments")
Repository(full_name="MeenakshiLalam/python_tasks")
