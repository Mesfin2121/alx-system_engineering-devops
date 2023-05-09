#!/usr/bin/python3
"""this script returns the number of subscribers 
(not active users, total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """this function is returns  the numbers of
    subscribers of a subreddit passed to it"""

    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    value = response.json().get('data').get('subscribers')
    if value:
        return value
    else:
        return 0
