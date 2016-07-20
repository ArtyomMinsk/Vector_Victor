class ShapeError(Exception):
    pass


def shape(vector):
    num_rows = len(vector)
    tup = tuple([num_rows])

    return tup

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
    num_sum = [vector_1[index] * vector_2[index] for index in range(len(vector_1))]
    return sum(num_sum)
