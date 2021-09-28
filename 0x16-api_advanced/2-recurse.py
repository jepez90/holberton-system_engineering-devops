#!/usr/bin/python3
"""
Defines the function number_of_subscribers
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """  queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url_api = 'https://www.reddit.com/'
    path = 'r/{}/hot/.json'.format(subreddit)
    url = url_api + path

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0', })
    query = {'limit': 100, 'after': after}

    # get info of the subreddit
    response = requests.get(
        url,
        allow_redirects=False,
        params=query,
        headers=headers
    )
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        data = data.get('data')
        for item in data.get('children'):
            hot_list.append(item.get('data').get('title'))

    response.close()
    if data.get('dist') == 100:
        return recurse(subreddit, hot_list, data.get('after'))
    else:
        return hot_list
