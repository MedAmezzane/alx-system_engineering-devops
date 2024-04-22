#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Extract employee ID from command-line argument
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information for the specified employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username from user information
    username = user.get("username")

    # Retrieve to-do list for the specified employee ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create and write to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({
            user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]
        }, jsonfile)
