#!/usr/bin/python3
"""
Defines the function number_of_subscribers
"""
import requests


def count_words(subreddit, word_list, after=None, hot_list=''):
    """  queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url_api = 'https://www.reddit.com/'
    path = 'r/{}/hot/.json'.format(subreddit)
    url = url_api + path

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Custom User Agent 1.0.1',
        "Content-Type": "application/json",
    })
    query = {'limit': 100, 'after': after, }

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
            hot_list += ' ' + item.get('data').get('title')

    response.close()

    if data.get('after') is None:
        # print the results
        dict_counter = {}
        hot_list = hot_list.casefold().split()
        for word in word_list:
            word_lower = word.casefold()
            if word_lower in dict_counter.keys():
                dict_counter[word_lower] += hot_list.count(word_lower)
            else:
                dict_counter[word_lower] = hot_list.count(word_lower)

        list_counter = list(dict_counter.items())
        list_counter.sort(key=lambda x: x[1], reverse=True)

        for item in list_counter:
            if item[1] != 0:
                print('{}: {}'.format(item[0], item[1]))

    else:
        count_words(subreddit, word_list, data.get('after'), hot_list)
