class ShapeError(Exception):
    pass



def shape(vector):
    if check_matrix_shape(vector):
        dimension = tuple([len(vector), len(vector[0])])
        return dimension
    else:
        num_rows = len(vector)
        tup = tuple([num_rows])
        return tup

    #matrix
    # dimension = tuple([len(matrix), len(matrix[0])])
    # return tup

def vector_add(vector_1, vector_2):
    if shape(vector_1) != shape(vector_2):
        raise ShapeError
    else:
        return [vector_1[index] + vector_2[index] for index in range(len(vector_1))]

def vector_sub(vector_1, vector_2):
    if shape(vector_1) != shape(vector_2):
        raise ShapeError
    else:
        return [vector_1[index] - vector_2[index] for index in range(len(vector_1))]

def vector_sum(*args):
    if not compare_shapes(*args):
        raise ShapeError
    else:
        return [sum(values) for values in zip(*args)]

def compare_shapes(*args):
    return len(set([shape(item) for item in args])) == 1

def dot(vector_1, vector_2):
    if not compare_shapes(vector_1, vector_2):
        raise ShapeError
    else:
        num_sum = [vector_1[index] * vector_2[index] for index in range(len(vector_1))]
        return sum(num_sum)

def vector_multiply(vector, number):
    return [vector[index] * number for index in range(len(vector))]

def vector_mean(*args):
    return [sum(value) / len(value) for value in zip(*args)]

def magnitude(vector):
    value_sum = sum([vector[index] ** 2 for index in range(len(vector))])
    return value_sum ** 0.5

# ADVANCED MODE

def check_matrix_shape(matrix):
    if type(matrix[0]) == list:
        return True

def matrix_row(matrix, index):
    return matrix[index]
