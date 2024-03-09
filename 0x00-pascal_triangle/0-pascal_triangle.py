#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    
    Args:
        n (int): The number of rows to generate in the triangle.
        
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Calculate element based on the sum of the elements above and to the left
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle

# Test the function
def print_triangle(triangle):
    """
    Prints the Pascal's triangle.
    
    Args:
        triangle (list): The Pascal's triangle to print.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Test cases
    print_triangle(pascal_triangle(5))  # Correct output: n = 5
    print_triangle(pascal_triangle(1))  # Correct output: n = 1
    print_triangle(pascal_triangle(0))  # Correct output: n = 0
    print_triangle(pascal_triangle(10))  # Correct output: n = 10
    # Printing Pascal's triangle with 100 rows might not be visually feasible, 
    # but we can still verify the correctness of the output.
    print_triangle(pascal_triangle(100))  # Correct output: n = 100
