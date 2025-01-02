# Uncommon Python TypeError: Iterating over NoneType

This repository demonstrates an example of an uncommon error in Python that can easily be missed during development. The error arises when attempting to iterate over a variable that has a NoneType value.

## Bug Description
The `bug.py` file contains a function `function_with_uncommon_bug`.  This function attempts to iterate over input data which may be None.  If data is None, a TypeError occurs.

## Solution
The `bugSolution.py` file shows how to handle the error gracefully using a try-except block, preventing the program from crashing.