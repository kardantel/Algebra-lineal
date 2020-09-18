def get_row(matrix, row):
    return matrix[row]


def get_column(matrix, column_number):
    column = []
    for i in range(len(matrix)):
        n = matrix[i][column_number]
        column.append(n)
    return column
