#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information for the specified employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Retrieve to-do list for the specified employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the summary of completed tasks for the employee
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the titles of completed tasks
    [print("\t {}".format(c)) for c in completed]
