import requests
import json
from datetime import datetime


def get_repo_info():
    response = requests.get("https://api.github.com/users/James-Welsh/repos")
    json_data = json.loads(response.content.decode('utf-8'))
    return json_data


def most_recent_repo():

    repos = get_repo_info()

    most_recent_repo = None

    for repo in repos:

        if most_recent_repo == None:
            most_recent_repo = repo
        else:
            current_repo_time = datetime.strptime(
                repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
            prev_repo_time = datetime.strptime(
                most_recent_repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")

            if current_repo_time > prev_repo_time:
                most_recent_repo = repo

    return most_recent_repo


def get_display_data():
    repo = most_recent_repo

    return {name: repo['name']}

