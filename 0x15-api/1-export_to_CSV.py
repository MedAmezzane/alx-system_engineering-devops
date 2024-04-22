#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    # Define the base URL for the JSONPlaceholder API
    url = 'https://jsonplaceholder.typicode.com/'

    # Get the user ID from the command line argument
    userid = sys.argv[1]

    # Construct the URL to retrieve user information based on the user ID
    user = '{}users/{}'.format(url, userid)
    res = requests.get(user)
    json_o = res.json()

    # Get the username from the user information
    name = json_o.get('username')

    # Construct the URL to retrieve tasks for the user
    todos = '{}todos?userId={}'.format(url, userid)
    res = requests.get(todos)
    tasks = res.json()

    # Create a list to store task information
    l_task = []

    # Loop through the tasks and append task details to the list
    for task in tasks:
        l_task.append([userid,
                       name,
                       task.get('completed'),
                       task.get('title')])

    # Create a filename for the CSV file based on the user ID
    filename = '{}.csv'.format(userid)

    # Open the CSV file in write mode
    with open(filename, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                      delimiter=',',
                                      quotechar='"',
                                      quoting=csv.QUOTE_ALL)

        # Write each task as a row in the CSV file
        for task in l_task:
            employee_writer.writerow(task)
