#!/usr/bin/python3
"""Module for recursively retrieving all hot post titles from a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot posts for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit.
        hot_list (list): Accumulator for post titles (used during recursion).
        after (str): Reddit API 'after' token for pagination.

    Returns:
        list: List of post titles, or None if subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    if not isinstance(subreddit, str) or subreddit == "":
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        # No more posts
        return hot_list

    for post in children:
        title = post.get("data", {}).get("title")
        if title is not None:
            hot_list.append(title)

    next_after = data.get("after")
    if next_after is None:
        # No more pages
        return hot_list

    # Recursive call with updated 'after'
    return recurse(subreddit, hot_list, next_after)
