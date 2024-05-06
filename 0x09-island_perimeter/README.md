# Island Perimeter

This project contains a Python function to calculate the perimeter of an island represented by a grid.

## Description

The function `island_perimeter(grid)` takes a grid as input, where 0 represents water and 1 represents land. It calculates and returns the perimeter of the island described by the grid. The island is assumed to be completely surrounded by water and has no lakes (water inside that isn't connected to the water surrounding the island).

## Requirements

- Python 3.4.3
- Ubuntu 20.04 LTS
- Editors: vi, vim, emacs

## Usage

To use the `island_perimeter` function, import it into your Python script and call it with the grid representing the island as input.

Example usage:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
