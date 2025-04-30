import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

for pull_request in complete_details:
    user = pull_request["user"]
    print(f"Login: {user['login']}, Node ID: {user['node_id']}")