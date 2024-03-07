#!/usr/bin/env python3
"""
This script defines a function pascal_triangle(n) that returns Pascal's triangle up to the specified number of rows 'n' as a list of lists of integers.
Returns an empty list if n <= 0.
"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows 'n'.
    
    Args:
        n (int): Number of rows in the Pascal's triangle.
        
    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
