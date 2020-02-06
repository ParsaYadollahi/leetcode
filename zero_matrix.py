'''
    CTCI question 1.8
'''


def zero_matrix(matrix):
    n = len(matrix[0])

    dic = {
        'column': [],
        'row': []
    }

    for col in range(n):
        for row in range(n):
            if matrix[col][row] == 0:
                dic['column'].append(col)
                dic['row'].append(row)

    for c in dic['column']:
        matrix = set_colum_zero(matrix, n, c)

    for r in dic['row']:
        matrix = set_row_zero(matrix, n, r)

    return matrix


def set_colum_zero(matrix, n, column):
    for i in range(n):
        matrix[column][i] = 0
    return matrix


def set_row_zero(matrix, n, row):
    for i in range(n):
        matrix[i][row] = 0
    return matrix


if __name__ == "__main__":
    print(zero_matrix([[0, 1, 0], [1, 1, 1], [1, 1, 1]]))
