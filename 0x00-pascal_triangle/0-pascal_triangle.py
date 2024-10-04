#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []
    triangle = [[1]]  # The first row is always [1]
    for i in range(1, n):
        row = [1]  # Start every row with a 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End every row with a 1
        triangle.append(row)
    return triangle
