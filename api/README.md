API

    Amateur
    By: Sylvain Kalache, co-founder at Holberton School
    Weight: 1
    Your score will be updated as you progress.

Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.
Resources

Read or watch:

    Friends don’t let friends program in shell script
    What is an API
    What is an API? In English, please
    What is a REST API
    What are microservices
    PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What Bash scripting should not be used for
    What is an API
    What is a REST API
    What are microservices
    What is the CSV format
    What is the JSON format
    Pythonic Package and module name style
    Pythonic Class name style
    Pythonic Variable name style
    Pythonic Function name style
    Pythonic Constant name style
    Significance of CapWords or CamelCase in Python

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.X)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    Libraries imported in your Python files must be organized in alphabetical order
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
    Your code should not be executed when imported (by using if __name__ == "__main__":)

Tasks
0. Gather data from an API

The Python script utilizes the requests module to interact with a given REST API, specifically designed for managing employee TODO lists. It takes an employee ID as a command line parameter and fetches information about the employee's progress on their TODO list from the API. The script then prints a summary on the standard output, adhering to the specified format:

    First Line: Displays the employee's name and the progress on tasks in the format:

    csharp

Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

    EMPLOYEE_NAME: The name of the employee.
    NUMBER_OF_DONE_TASKS: The number of completed tasks.
    TOTAL_NUMBER_OF_TASKS: The total number of tasks, including both completed and non-completed tasks.

Subsequent Lines: Display the titles of completed tasks with one tabulation and one space before each task title:

markdown

         TASK_TITLE

        TASK_TITLE: The title of a completed task.

The script ensures proper error handling for potential issues during API requests and follows the specified guidelines for formatting and output. 

Repo:

    GitHub repository: holbertonschool-back-end
    Directory: api
    File: 0-gather_data_from_an_API.py

0/7 pts
1. Export to CSV

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv

Repo:

    GitHub repository: holbertonschool-back-end
    Directory: api
    File: 1-export_to_CSV.py

0/5 pts
1. Export to JSON
mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json

Repo:

    GitHub repository: holbertonschool-back-end
    Directory: api
    File: 2-export_to_JSON.py

0/5 pts
1. Dictionary of list of dictionaries
mandatory

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

    Records all tasks from all employees
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json

Repo:

    GitHub repository: holbertonschool-back-end
    Directory: api
    File: 3-dictionary_of_list_of_dictionaries.py

