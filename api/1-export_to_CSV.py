#!/usr/bin/python3

"""Export to CSV"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Returns information about his/her TODO list progress.
    """
    # Get the user's tasks through the API
    todo_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))

    # Check if the requests were successful
    if todo_response.status_code != 200 or user_response.status_code != 200:
        print("Error fetching data from the API.")
        return

    todo_data = todo_response.json()  # Parse user's tasks to JSON
    user_data = user_response.json()  # Parse user data to JSON
    employee_name = user_data['name']

    # Print the user's tasks
    print("Employee {} is done with tasks:".format(employee_name))
    for task in todo_data:
        print("\t{}".format(task['title']))

    # Export tasks to CSV
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write CSV header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write task data
        for task in todo_data:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])

    print("Data exported to {}".format(csv_filename))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
