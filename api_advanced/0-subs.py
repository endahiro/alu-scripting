#!/usr/bin/python3
"""Module for querying Reddit API for subreddit subscriber counts."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alu-scripting:v1.0 (by u/alu_student_bot)"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
    except requests.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)
