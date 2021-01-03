from typing import List
from math import gcd
from fractions import Fraction

"""
example matrix:
[
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
"""

def transform_matrix(m: List[List]):
    """
    example matrix becomes
    [
        [0, 1/2, 0, 0, 0, 1/2],
        [4/9, 0, 0, 1/3, 2/9, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1]
    ]
    """
    l = len(m)
    for i in range(l):
        row_sum = sum(m[i])
        if row_sum == 0:
            m[i][i] = 1
        else:
            for j in range(l):
                m[i][j] = Fraction(m[i][j], row_sum)

def get_submatrix(matrix: List[List], rows: List, cols: List) -> List[List]:
    new_matrix = []
    for row in rows:
        current_row = []
        for col in cols:
            current_row.append(matrix[row][col])
        new_matrix.append(current_row)
    return new_matrix

def get_q_matrix(matrix: List[List], transient_states: List) -> List[List]:
    """
    For example matrix
    q_matrix = [
        [0, 1/2],
        [4/9, 0]
    ]
    """
    return get_submatrix(matrix, transient_states, transient_states)

def get_r_matrix(matrix: List[List], transient_states: List, absorbing_states: List) -> List[List]:
    """
    For example matrix
    r_matrix = [
        [0, 0, 0, 1/2],
        [0, 1/3, 2/9, 0]
    ]
    """
    return get_submatrix(matrix, transient_states, absorbing_states)

def make_2d_list(n: int, m: int) -> List[List]:
    a = []
    for row in range(n):
        a += [[0]*m]
    return a

def make_identity(n: int) -> List[List]:
    """
    for n=3, it returns
    [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    """
    matrix = make_2d_list(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def subtract_matrices(a: List[List], b: List[List]) -> List[List]:
    new_matrix = []
    n, m = len(a), len(b)
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[i][j] - b[i][j])
        new_matrix.append(row)
    return new_matrix

def multiply_matrices(a: List[List], b: List[List]) -> List[List]:
    """
    Multiply two matrices a and b
    matrix a of size A X B and matrix b of size B X C
    would yield a matrix c of size A X C
    """
    ar, ac, bc = len(a), len(a[0]), len(b[0])
    c = make_2d_list(ar, bc)
    for i in range(ar):
        for j in range(bc):
            prod = Fraction(0, 1)
            for k in range(ac):
                prod += a[i][k] * b[k][j]
            c[i][j] = prod
    return c

def multiply_row_of_square_matrix(matrix: List[List], row: int, k: int) -> List[List]:
    n = len(matrix)
    identity = make_identity(n)
    identity[row][row] = k
    return multiply_matrices(identity, matrix)

def add_multiple_of_row_of_square_matrix(matrix: List[List], source_row: int, k: int, target_row: int):
    """
    add k * source_row to target_row of matrix m
    """
    n = len(matrix)
    row_operator = make_identity(n)
    row_operator[target_row][source_row] = k
    return multiply_matrices(row_operator, matrix)

def invert_matrix(matrix: List[List]) -> List[List]:
    n = len(matrix)
    inverse = make_identity(n)
    for col in range(n):
        diagonal_row = col
        k = Fraction(1, matrix[diagonal_row][col])
        matrix = multiply_row_of_square_matrix(matrix, diagonal_row, k)
        inverse = multiply_row_of_square_matrix(inverse, diagonal_row, k)
        source_row = diagonal_row
        for target_row in range(n):
            if source_row != target_row:
                k = -matrix[target_row][col]
                matrix = add_multiple_of_row_of_square_matrix(matrix, source_row, k, target_row)
                inverse = add_multiple_of_row_of_square_matrix(inverse, source_row, k, target_row)
    return inverse

def lcm(a: int, b: int) -> int:
    result = a * b // gcd(a, b)
    return result

def lcm_for_arrays(args: List) -> int:
    array_length = len(args)
    if array_length <= 2:
        return lcm(*args)

    initial = lcm(args[0], args[1])
    i = 2
    while i < array_length:
        initial = lcm(initial, args[i])
        i += 1
    return initial

def solution(m):
    """
    For example matrix
    transient_states = [0, 1]
    absorbing_states = [2, 3, 4, 5]
    """
    transient_states = []
    absorbing_states = []
    for i in range(len(m)):
        row = m[i]
        if sum(row) == 0:
            absorbing_states.append(i)
        else:
            transient_states.append(i)

    transform_matrix(m)

    q = get_q_matrix(m, transient_states)
    r = get_r_matrix(m, transient_states, absorbing_states)
    identity = make_identity(len(q))
    diff = subtract_matrices(identity, q)
    inverse = invert_matrix(diff)
    result = multiply_matrices(inverse, r)
    print('initial result', result)

    denominator = lcm_for_arrays([item.denominator for item in result[0]])
    result = [item.numerator * denominator // item.denominator for item in result[0]]
    result.append(denominator)
    return result

if __name__ == "__main__":
    m1 = [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(solution(m1))
    