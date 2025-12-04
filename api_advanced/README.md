# 🔥 Reddit API – Advanced (How to Run Locally + Project Documentation)

This project contains Python functions that interact with the Reddit API.  
Each function can be tested locally by using short Python commands.

---

# 🚀 HOW TO RUN LOCALLY (TOP SECTION)

Make sure you are inside the project directory:

```bash
cd ~/alu-projects/alu-scripting/api_advanced
```

On Windows, use **python** or **py**, NOT python3.

Install required module:

```bash
python -m pip install requests
```

---

## ▶️ Task 0 – `number_of_subscribers()`

Returns the number of subscribers for a subreddit.

**Run locally:**

```bash
python -c "number_of_subscribers = __import__('0-subs').number_of_subscribers; print(number_of_subscribers('programming'))"
python -c "number_of_subscribers = __import__('0-subs').number_of_subscribers; print(number_of_subscribers('fake_subreddit_123'))"
```

---

## ▶️ Task 1 – `top_ten()`

Prints the titles of the top 10 hot posts of a subreddit.

**Run locally:**

```bash
python -c "top_ten = __import__('1-top_ten').top_ten; top_ten('programming')"
python -c "top_ten = __import__('1-top_ten').top_ten; top_ten('fake_subreddit_123')"
```

Expected:
- Valid subreddit → prints 10 lines (titles)
- Invalid subreddit → prints:
```
None
```

---

## ▶️ Task 2 – `recurse()`

Recursively returns a list of all hot post titles.

**Run locally:**

```bash
python -c "recurse = __import__('2-recurse').recurse; res = recurse('programming'); print(len(res) if res else 'None')"
python -c "recurse = __import__('2-recurse').recurse; print(recurse('fake_subreddit_123'))"
```

---

## ▶️ Task 3 – `count_words()`

Recursively counts keyword occurrences in hot post titles.

**Run locally:**

```bash
python -c "count_words = __import__('3-count').count_words; count_words('programming', ['java', 'python', 'javascript', 'scala'])"
python -c "count_words = __import__('3-count').count_words; count_words('programming', ['Java', 'java'])"
python -c "count_words = __import__('3-count').count_words; count_words('fake_subreddit_123', ['python'])"
```

Expected:
- Prints counts sorted by:
  1. Count (descending)
  2. Word (alphabetically ascending)
- Invalid subreddit → prints nothing

---

# 🛠 Project Requirements (ALU)

- Python 3.4.3 compatible
- Must use `requests` module
- Must set custom `User-Agent`
- Must NOT follow redirects
- Must handle invalid subreddits gracefully
- Must follow PEP8:

```bash
python -m pycodestyle 0-subs.py
python -m pycodestyle 1-top_ten.py
python -m pycodestyle 2-recurse.py
python -m pycodestyle 3-count.py
```

---
