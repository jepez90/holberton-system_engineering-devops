#!/usr/bin/python3
""" using this REST API, for a given employee ID, returns information about
    his/her TODO list progress.
"""

import json
import requests

if __name__ == '__main__':
    url_api = 'https://jsonplaceholder.typicode.com/'
    path = 'users/'

    # get info of the user
    response = requests.get(url_api + path)
    data_user = response.json()
    response.close()

    output = {}

    for user in data_user:
        # get info of the todos for each user
        url = '{}{}{}/todos'.format(url_api, path, user.get('id'))
        response = requests.get(url)
        data_todos = response.json()
        response.close()

        # make list of tasks one dict for each
        tasks_list = []

        for todo in data_todos:
            task = {}
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            task['username'] = user.get('username')
            tasks_list.append(task)

        # make a dictionary with user_id:tasklist
        output[user.get('id')] = tasks_list

    # write otput to file as json
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(output, file)
