#!/usr/bin/python3

"""Python script to export data in the JSON format
"""
"""import json
import requests
from collections import defaultdict

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def export_all_to_json():
    Export all tasks from all employees to JSON

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
    export_all_to_json()"""
    
import json
import requests
from sys import argv


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        tasks = requests.get(base_url + "todos",
                        params={"userId": user_id}).json()

        task_list = []
        for task in tasks:
            task_list.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            })

        all_data[user_id] = task_list

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
