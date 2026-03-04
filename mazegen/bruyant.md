# Common Instructions
- type hints for:
  - funcs params
  - vars

- mypy: for static checking

- docstrings to document:
  - purpose
  - params
  - returns

- Makefile:
  - install
  - returns
  - debug
  - clean
  - lint
  - lint-strict (optional)

- 
-----

# Mandatory
- summary:
  - parse a config file
  - generate maze
  - write it to a file using hexadecimal wall representation
  - visual representation
  - organize so the generation logic can be reused

Usage:
- python3 a_maze_ing.py config.txt
- handle:
  - invalid configuration
  - file not found
  - bad syntax
  - impossible maze parameters
  - ...
  - always provide a clear error message to the user.
