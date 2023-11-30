#!/usr/bin/python3
"""
Pascal's Triangle Generator
This module def a fnctn for generatn Pascal's Triangle based on given rows.
"""


def pascal_triangle(n):
    """
    Parameters:
        n (int): The number of rows to generate .

    Returns:
        list: A list of lists representing Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Run the test cases using pytest
    pytest.main([__file__])
