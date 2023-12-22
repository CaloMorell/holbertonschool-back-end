#!/usr/bin/python3

"""Export to CSV"""


import csv
import requests

def export_to_csv(user_id):
    # Make API request to get user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user = user_response.json()

    # Make API request to get user tasks
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    tasks = tasks_response.json()

    # Write data to CSV file
    with open(f'{user_id}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks data
        for task in tasks:
            writer.writerow([user_id, user['username'], task['completed'], task['title']])

if __name__ == "__main__":
    # Example: Export tasks for user with ID 1
    export_to_csv(1)
