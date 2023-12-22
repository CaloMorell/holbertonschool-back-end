#!/usr/bin/python3

"""Python script to export data in the JSON format
"""
import json
import requests
from collections import defaultdict

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def export_all_to_json():
    """ Export all tasks from all employees to JSON """

    correct_output = defaultdict(list)

    # Map userId to username to avoid multiple API requests for the same user
    user_names = {}

    try:
        user_response = requests.get(users_url[:-1])  # Get all users
        user_data = user_response.json()
        for user in user_data:
            user_names[user['id']] = user['username']

        todo_response = requests.get(todos_url)
        todo_data = todo_response.json()

        for item in todo_data:
            user_id = item['userId']
            username = user_names.get(user_id, "Unknown")
            correct_output[user_id].append({
                'username': username,
                'task': item['title'],
                'completed': item['completed']
            })

    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        sys.exit(1)

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(correct_output, jsonfile)


if __name__ == "__main__":
    export_all_to_json()
