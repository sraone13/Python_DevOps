
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sravanpeddapally.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0jGHDsE2HdfYiR6NpNcivJs9YtZWqrqg8f2MIJJ9V28xslriX7BmMyahlm1FtV_0OWdHyp5Z_Gei8D5gK3Md5OKqB_TDiNCAvGUe9zUd5sweUbosrAQH2nUDcRTwSDZz3cJv96KArXlsYl9sM-UhVfczknpE13WTA5ORt9435IDc=CDF06949"

auth = HTTPBasicAuth("sravanpeddapally@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# Print only project names
projects = response.json()

for project in projects:
    print(project.get("name"))