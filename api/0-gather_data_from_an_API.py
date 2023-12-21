#!/usr/bin/python3
"""The script ensures proper error handling for potential issues during API
requests and follows the specified guidelines for formatting and output. """

import json as json
from collections import OrderedDict
import requests
from sys import argv



if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if user_response.status_code == 200:
        employee_name = user_data.get("username", "")
        if not employee_name:
            print("Error: Unable to fetch employee name.")
            exit()

        todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
        todo_response = requests.get(todo_url)

        if todo_response.status_code == 200:
            todos = todo_response.json()

            if todos:
                total_tasks = len(todos)
                completed_tasks = sum(1 for todo in todos if todo["completed"])

                print("Employee {} is done with tasks ({}/{}):".format(
                    employee_name, completed_tasks, total_tasks))

                for idx, todo in enumerate(todos, start=1):
                    if todo["completed"]:
                        print("\t {}. {}".format(idx, todo["title"]))
            else:
                print("Employee {} has no tasks.".format(employee_name))
        else:
            print("Error: Unable to fetch TODO list data from API")
    else:
        print("Error: Unable to fetch user data from API")
