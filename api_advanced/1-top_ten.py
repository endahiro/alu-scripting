#!/usr/bin/python3
"""Module for querying Reddit API for top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    If the subreddit is invalid or has no hot posts, prints 'None'.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    posts = data.get("children", None)

    if not posts:
        print("None")
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
