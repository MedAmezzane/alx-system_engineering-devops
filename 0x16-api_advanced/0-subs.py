#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: The total number of subscribers, or 0 if the input is invalid.
    """
    # Check if the subreddit is a valid string
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Make a GET request to the Reddit API to fetch subreddit information
    api_url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    response = requests.get(api_url, headers=headers).json()

    # Extract the number of subscribers from the API response
    subscribers = response.get("data", {}).get("subscribers", 0)

    return subscribers
