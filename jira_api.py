import requests
import json
from datetime import datetime, timedelta

# author: Utku Boran Torun
# version 15.03.2022

# This code snippet finds closed ANY23 porject's issues for certain conditions

# JIRA REST API endpoint
jira_url = "https://issues.apache.org/jira/rest/api/2/search"

# JQL query to retrieve closed issues from the ANY23 project for the last month
jql_query = "project=ANY23 AND status=Closed AND resolutionDate >= startOfMonth(-24)" # it can be changed to createdDate >= startOfMonth(MONTH)

# JIRA API request headers
headers = {
    "Accept": "application/json"
}

# JIRA API request parameters
params = {
    "jql": jql_query,
    "maxResults": 100,
    "fields": "summary,description,assignee"
}

# Make the JIRA API request
response = requests.get(jira_url, headers=headers, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Print the results
for issue in data["issues"]:
    print("Title:", issue["fields"]["summary"])
    print("Description:", issue["fields"]["description"])
    if issue["fields"]["assignee"] is not None:
        print("Assignee:", issue["fields"]["assignee"]["displayName"])
    else:
        print("Assignee: None")
    print("------------------")

# To print in JSON format
#print(json.dumps(data, indent=4))
