# Redis Basic Project

## Project Overview

This project introduces the basics of using **Redis** in Python for various data caching and tracking use cases. It covers how to use Redis as a data store, a cache, and a tool for observability through tracking function calls and their histories.

This project was done as part of the ALU Holberton School curriculum and includes tasks such as writing to and reading from Redis, using decorators for counting and logging, and implementing a basic web cache with expiration.

---

## Technologies Used

- Language: Python 3.7+
- Redis: Server and Python Client (`redis-py`)
- System: Ubuntu 18.04 LTS
- Tools: `uuid`, `functools`, `requests`

---

## Setup Instructions

### Install Redis and Python Dependencies

```bash
sudo apt-get -y install redis-server
pip3 install redis requests
````

Ensure Redis is configured to run locally:

```bash
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
sudo service redis-server start
```

---

## Project Files

### `exercise.py`

Implements the following:

#### `Cache` Class

* `__init__`: Initializes Redis client and flushes DB.
* `store`: Stores data under a random UUID key.
* `get`: Retrieves and decodes data with optional format conversion.
* `get_str`: Helper to decode data as UTF-8 string.
* `get_int`: Helper to convert data to int.

#### Decorators

* `count_calls`: Increments Redis counter every time a method is called.
* `call_history`: Records inputs and outputs of method calls.

#### Utility Function

* `replay(fn)`: Replays the history of calls to a given function.

---

### `web.py`

Implements:

#### `get_page(url: str) -> str`

* Fetches web page content using `requests.get`.
* Tracks access count using key `count:{url}`.
* Caches content for 10 seconds in Redis.

---

## Learning Objectives

* Understand how to use Redis for basic string/byte storage and retrieval.
* Implement method call counting and call history tracking using decorators.
* Use Redis to cache web content with expiration.
* Apply Python type annotations and good docstring practices.

---

## Usage Examples

```python
# Storing and retrieving data
cache = Cache()
key = cache.store("hello")
print(cache.get(key, fn=lambda x: x.decode()))

# Checking call counts and history
replay(cache.store)

# Caching a web page
from web import get_page
html = get_page("http://slowwly.robertomurray.co.uk/delay/5000/url/http://example.com")
```

---

## Author

**Daniel Iryivuze**
Redis Basic Project - ALU 
---

## Status

✅ All mandatory tasks completed
✅ All functions and methods fully documented
✅ Type annotations added
✅ pycodestyle compliant
✅ Bonus task implemented (partially)

```