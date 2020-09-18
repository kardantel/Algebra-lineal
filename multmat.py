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


def matrix_multiplication(matrixA, matrixB):
    '''Función que multiplica las matrices.'''
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    result = []  # lista vacia que almacena el producto de AxB
    for i in range(m_rows):
        row_result = []  # matriz para mantener la fila del producto punto.
        rowA = get_row(matrixA, i)
        for j in range(p_columns):
            columnB = get_column(matrixB, j)
            prod_punto = dot_product(rowA, columnB)
            row_result.append(prod_punto)
        result.append(row_result)
    return result
