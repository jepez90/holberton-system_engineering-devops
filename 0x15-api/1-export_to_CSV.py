#!/usr/bin/python3
# using this REST API, for a given employee ID, returns information about
# his/her TODO list progress.

from sys import argv
import requests

if __name__ == '__main__':
    user_id = argv[1]
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

    with open(user_id + '.csv', mode='w') as file:
        for task in data_todos:
            file.write('"{}","{}","{}","{}"\n'.format(
                data_user.get('id'),
                data_user.get('name'),
                task.get('completed'),
                task.get('title')
            ))
