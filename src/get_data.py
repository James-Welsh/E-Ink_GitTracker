import requests
import json
from datetime import datetime


def get_repo_info():

    key_file = open('key.txt', 'r')
    key = key_file.read().strip('\n') #Gets the token and removes the '\n'
    key_file.close()
    
    #The header for the API request allowing private repos to be viewed as well
    headers = {
        "Authorization": ("token " + key),
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get("https://api.github.com/user/repos", headers=headers)
    json_data = json.loads(response.content.decode('utf-8'))

    return json_data #Returns the data as a JSON object


def most_recent_repo():

    repos = get_repo_info()

    most_recent_repo = None #Initalise variable

    for repo in repos:

        if most_recent_repo == None: #If this is the first repo looked at
            most_recent_repo = repo
        else:
            current_repo_time = datetime.strptime(
                repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ") #Formatting gitHubs time
            prev_repo_time = datetime.strptime(
                most_recent_repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")

            #If current repo was updated after the repo currently in 'most_recent_repo'
            if current_repo_time > prev_repo_time:
                most_recent_repo = repo

    return most_recent_repo #return the most recent Repo


def get_display_data():
    repo = most_recent_repo()

    time = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
    formated_time = datetime.strftime(time, "%d/%m/%Y %H:%M:%S") #Format time nicely

    privacy = "Public" #default privacy varaible

    if repo['private'] : #if repo is private
        privacy = "Private"

    data = {
        'name': repo['name'],
        'updated': formated_time,
	'privacy': privacy

    } #A dictionary of data to return

    return data

