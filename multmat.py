def get_row(matrix, row):
    '''Función que extrae filas.'''
    return matrix[row]


def get_column(matrix, column_number):
    '''Función que extrae columnas.'''
    column = []
    for i in range(len(matrix)):
        n = matrix[i][column_number]
        column.append(n)
    return column


def dot_product(vector_one, vector_two):
    '''Función que realiza producto punto.'''
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
