#!/usr/bin/python3
""" using this REST API, for a given employee ID, returns information about
    his/her TODO list progress.
"""

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_api = 'https://jsonplaceholder.typicode.com/'
    path = 'users/'

    # get info of the user
    response = requests.get(url_api + path + user_id)
    data_user = response.json()
    response.close()

    # get info of the todos
    response = requests.get(url_api + path + user_id + '/todos')
    data_todos = response.json()
    response.close()

    # make list of tasks one dict for each
    tasks_list = []

    for todo in data_todos:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = data_user.get('name')
        tasks_list.append(task)

    # make a dictionary with user_id:tasklist
    output = {}
    output[user_id] = tasks_list

    # write otput to file as json
    with open(user_id + '.json', mode='w') as file:
        json.dump(output, file)
