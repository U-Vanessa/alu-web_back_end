# Python - Variable Annotations

## Python Type Annotations

This project explores the implementation and usage of type annotations in Python 3, focusing on how they enhance code readability, maintainability, and reduce potential bugs through static type checking.

### Learning Objectives

By the end of this project, you should be able to explain:

* Type annotations in Python 3
* How to use type annotations to specify function signatures and variable types
* Duck typing concepts and implementation
* How to validate your code with `mypy`

### Requirements

#### General

* All files are interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/env python3`
* Code should follow the `pycodestyle` style (version 2.5)
* All files must be executable
* All modules, classes, and functions must include appropriate documentation
* Documentation should be comprehensive sentences explaining the purpose of modules, classes, or methods

### Concepts Overview

#$## Type Annotations in Python 3

Type annotations were introduced in Python 3.5 through PEP 484. They provide a way to indicate the expected types of variables, function parameters, and return values. While Python remains dynamically typed, these annotations serve as hints to developers and tools.

```python
def greeting(name: str) -> str:
    return f"Hello, {name}"
```

#### Function Signatures and Variable Types

Type annotations enable specifying expected data types for:

* Function parameters: `def process_data(data: list) -> None:`
* Function return values: `def calculate_sum(a: int, b: int) -> int:`
* Variables: `user_id: int = 42`

#### Duck Typing

Duck typing is a programming concept where the type or class of an object is less important than the methods it defines or the properties it has. The name comes from the saying: "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

Python is inherently duck-typed, but type annotations can help clarify expected behaviors while maintaining flexibility.

#### Validating Code with `mypy`

`mypy` is a static type checker for Python that helps catch common errors before runtime:

```bash
pip install mypy
mypy your_file.py
```

### Project Structure

This repository contains various examples and implementations demonstrating Python type annotations and related concepts.

### Author

Vanessa UWONKUNDA
