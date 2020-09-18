def get_row(matrix, row):
    return matrix[row]


def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        n = matrix[i][column_number]
        column.append(n)
    return column


def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
