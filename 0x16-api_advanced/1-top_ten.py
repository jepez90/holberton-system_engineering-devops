#!/usr/bin/python3
"""
Defines the function number_of_subscribers
"""
import requests


def top_ten(subreddit):
    """  queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url_api = 'https://www.reddit.com/'
    path = 'r/{}/hot/.json'.format(subreddit)
    url = url_api + path

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0', })
    query = {'limit': 10}

    # get info of the subreddit
    response = requests.get(
        url,
        allow_redirects=False,
        params=query,
        headers=headers
    )
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        data = data.get('data').get('children')
        for item in data:
            print(item.get('data').get('title'))
    response.close()
