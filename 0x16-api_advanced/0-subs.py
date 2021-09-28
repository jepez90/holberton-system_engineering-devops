#!/usr/bin/python3
"""
Defines the function number_of_subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    url_api = 'https://www.reddit.com/'
    path = 'r/{}/about/.json'.format(subreddit)

    # get info of the subreddit
    response = requests.get(url_api + path, allow_redirects=False)

    if response.status_code != 200:
        response.close()
        return 0

    data = response.json()
    response.close()

    return(data.get('data').get('subscribers'))
