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
    # if shape(args) != shape(args):
    #     raise ShapeError
    # else:
    return [sum(values) for values in zip(*args)]

# def dot(vector_1, vector_2):
#
#     return [vector_1[index] * vector_2[index] for index in range(len(vector_1))]
