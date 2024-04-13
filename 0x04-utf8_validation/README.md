# UTF-8 Validation

This module provides a function to determine if a given data set represents a valid UTF-8 encoding. It checks a list of integers, where each integer represents a byte of data, to see if it conforms to the UTF-8 encoding rules.

## Function: validUTF8(data)

### Description

The `validUTF8` function takes a list of integers (`data`) as input and checks if it represents a valid UTF-8 encoding. It returns `True` if the data is valid UTF-8, otherwise `False`.

### Parameters

- `data`: A list of integers representing bytes of data.

### Returns

- `bool`: `True` if `data` is a valid UTF-8 encoding, else `False`.

## Usage

To use the `validUTF8` function, import it from `0-validate_utf8.py` and call it with a list of integers as shown below:

```python
from 0-validate_utf8 import validUTF8

# Test cases
data1 = [65]
print(validUTF8(data1))  # Output: True

data2 = [240, 188, 128, 167]
print(validUTF8(data2))  # Output: True

data3 = [345, 467]
print(validUTF8(data3))  # Output: False
