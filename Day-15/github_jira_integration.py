from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)


@app.route('/createJira', method=['POST'])
def createJira():

    url = "https://sravanpeddapally.atlassian.net/rest/api/3/issue"
    
    API_TOKEN = ""

    auth = HTTPBasicAuth("sravanpeddapally@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My 3rd Jira for Testing ",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "project": {
        "key": "SCRUM"
        },
        "issuetype": {
        "id": "10002"
        },
        "summary": "My 3rd"
        " BUG Jira",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

   return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


#Github integration with Jira to create the issues complete automation
#Github -- git repo webhook --> ec2 instance python script --> Jira issues create

