# API Tasks

This repository contains Python scripts to interact with a REST API and perform various tasks related to managing employee TODO lists.

## Requirements

- **GitHub Repository:** [holbertonschool-back-end]
- **Directory:** [api]

## Task 0: Gather data from an API

### Description
Write a Python script that, using a specified REST API, gathers information about a given employee's TODO list progress.

### Requirements
- Use of `urllib` or `requests` module
- Accept an integer as a parameter (employee ID)
- Display employee TODO list progress in the specified format

### Script
- **File:** [0-gather_data_from_an_API.py]

## Task 1: Export to CSV

### Description
Extend the Python script from Task 0 to export data in CSV format.

### Requirements
- Record all tasks owned by the specified employee
- Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name: USER_ID.csv

### Script
- **File:** [1-export_to_CSV.py]

## Task 2: Export to JSON

### Description
Extend the Python script from Task 0 to export data in JSON format.

### Requirements
- Record all tasks owned by the specified employee
- Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name: USER_ID.json

### Script
- **File:** [2-export_to_JSON.py]

## Task 3: Dictionary of list of dictionaries

### Description
Extend the Python script from Task 0 to export data in JSON format for all employees.

### Requirements
- Record all tasks from all employees
- Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name: todo_all_employees.json

### Script
- **File:** [3-dictionary_of_list_of_dictionaries.py]

