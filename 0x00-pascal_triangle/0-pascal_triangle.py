#!/usr/bin/python3

def pascal_triangle(n):
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
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
