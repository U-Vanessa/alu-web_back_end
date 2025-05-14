# Python - Async Comprehension

I have done this project as part of the ALU Web Backend curriculum to understand how asynchronous generators and comprehensions work in Python.

This project helped me learn how to:

* Write asynchronous generators using async def and yield
* Use async comprehensions to collect data from async iterables
* Execute coroutines concurrently using asyncio.gather
* Type-annotate asynchronous functions and generators

---

## Tasks Overview

### 0. Async Generator

Created a coroutine called async\_generator that yields 10 random floats between 0 and 10, one per second.

📁 File: 0-async\_generator.py

---

### 1. Async Comprehensions

Used an async comprehension to collect 10 random numbers from async\_generator and return them as a list.

📁 File: 1-async\_comprehension.py

---

### 2. Runtime for Four Parallel Comprehensions

Ran async\_comprehension four times in parallel and measured total runtime using asyncio.gather. The total execution time is around 10 seconds since all comprehensions run concurrently.

📁 File: 2-measure\_runtime.py

---

## Requirements

* Python 3.7
* Follows pycodestyle (v2.5.x)
* All files are executable and include documentation and type hints

---

## Author

Daniel Iryivuze