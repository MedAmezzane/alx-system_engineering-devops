#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import csv
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

    # Create and write to CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write each to-do item to the CSV file
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
