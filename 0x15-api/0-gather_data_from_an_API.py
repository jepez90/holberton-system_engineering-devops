#!/usr/bin/python3
""" using this REST API, for a given employee ID, returns information about
    his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url_api = 'https://jsonplaceholder.typicode.com/'
    path = 'users/'
    response = requests.get(url_api + path + user_id)
    data_user = response.json()
    response.close()

    response = requests.get(url_api + path + user_id + '/todos')
    data_todos = response.json()
    response.close()
    completed_tasks = ''
    completed_tasks_count = 0
    for task in data_todos:
        if task.get('completed'):
            completed_tasks += '\t {}\n'.format(task.get('title'))
            completed_tasks_count += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        data_user.get('name'),
        completed_tasks_count,
        len(data_todos))
    )
    print(completed_tasks, end='')
