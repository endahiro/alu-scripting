#!/usr/bin/python3
"""Recursive count of keywords in subreddit hot article titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count occurrences of words in the titles of hot posts.

    Args:
        subreddit (str): Name of the subreddit.
        word_list (list): List of keywords to count (case-insensitive).
        after (str): Reddit API 'after' token for pagination (used internally).
        counts (dict): Accumulator for word counts (used internally).

    Prints:
        Lines in the format 'word: count' sorted by count desc, then word asc.
        Prints nothing if subreddit is invalid or no matches are found.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        return

    # First call: initialize counts dict and normalize words
    if counts is None:
        if not word_list:
            return

        counts = {}
        for w in word_list:
            key = w.lower()
            counts[key] = counts.get(key, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My User Agent 1.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    children = data.get("children", [])

    # Process this page of posts
    for post in children:
        title = post.get("data", {}).get("title", "").lower()
        # Split by spaces; do not strip punctuation so 'java.' != 'java'
        for token in title.split():
            if token in counts:
                counts[token] += 1

    next_after = data.get("after")
    if next_after is not None:
        # Recursive call for next page
        return count_words(subreddit, list(counts.keys()), next_after, counts)

    # No more pages: print results
    filtered = {w: c for w, c in counts.items() if c > 0}
    if not filtered:
        return

    sorted_items = sorted(
        filtered.items(),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_items:
        print("{}: {}".format(word, count))
