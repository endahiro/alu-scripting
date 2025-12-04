#!/usr/bin/python3
"""Module for querying Reddit API for top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    If the subreddit is invalid, prints 'None'.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "alu-scripting:v1.0 (by u/alu_student_bot)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        print("None")
        return

    for post in children:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
