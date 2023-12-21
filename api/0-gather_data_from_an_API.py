#!/usr/bin/python3
"""The script ensures proper error handling for potential issues during API
requests and follows the specified guidelines for formatting and output. """

"""import requests
import sys

def make_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error during request: {e}')
        return None

def get_employee_todo_progress(employee_id):
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    # Make API requests
    todos = make_api_request(todos_url)
    user_data = make_api_request(user_url)

    if todos is None or user_data is None:
        # Exit or handle errors accordingly
        sys.exit(1)

    # Extract relevant information
    employee_name = user_data.get('name', f'Employee {employee_id}')
    done_tasks = [todo['title'] for todo in todos if todo['completed']]
    total_tasks = len(todos)

    # Display the information in the specified format
    print(f'Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):')
    print(f'\t{employee_name}: {len(done_tasks)}/{total_tasks}')

    for task_title in done_tasks:
        print(f'\t {task_title}')

if __name__ == '__main__':
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 2:
        print('Usage: python script.py <EMPLOYEE_ID>')
        sys.exit(1)

    # Get the employee ID from the command line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print('Invalid employee ID. Please provide a valid integer.')
        sys.exit(1)

    # Call the function with the provided employee ID
    get_employee_todo_progress(employee_id)"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        sys.exit(1)

    employee_name = data[0]["user"]["name"]
    total_tasks = len(data)
    done_tasks = [task for task in data if task["completed"]]
    total_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
        f"({total_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")
