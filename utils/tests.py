from general_utils import multiply_matrices, permute_feature_vector, create_diagonal_matrix, generate_lower_triangular_matrix
import numpy as np

def test_multiply_matrices():

    M1 = [[1, 0, 1, 2, 3, 1, 0],
    [0, 1, 2, 1, 1, 0, 1],
    [1, 1, 1, 0, 2, 1, 0],
    [0, 2, 1, 2, 1, 0, 1],
    [1, 1, 0, 1, 2, 1, 0],
    [1, 0, 0, 0, 2, 2, 1],
    [0, 2, 2, 1, 2, 0, 1]]

    M2 = [[1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [0, 3, 0, 2, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 2, 1],
    [0, 2, 0, 1, 0, 0, 0]]


    F1 = [[0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, -3, 0, 0, 0],
    [0, 0, 0, 0, -34, 0, 0],
    [0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 1]]


    Sf = [[1,0,0,0,0,0,0],
          [0,1,0,0,0,0,0],
          [1,1,1,0,0,0,0],
          [0,1,0,1,0,0,0],
          [1,0,1,1,1,0,0],
          [0,0,0,0,0,1,0],
          [1,2,0,2,0,1,1]]


    matrices = [np.array(M1, dtype='float'),np.array(Sf, dtype='float'),np.array(F1, dtype='float'),np.array(M2, dtype='float')]
    res = multiply_matrices(matrices)

    print(res)

def test_permute_feature_vector():

    feature_vec = [-3, 5, 1, -34, 1, 0, 2]
    permutation = [6, 2, 5, 1, 4, 7, 3]

    permuted_feature_vector = permute_feature_vector(feature_vec, permutation)

    print(permuted_feature_vector)

def test_create_diagonal_matrix():

    feature_vec = [-3, 5, 1, -34, 1, 0, 2]
    matrix = create_diagonal_matrix(feature_vec)

    print(matrix)

def test_generate_lower_triangular_matrix():

    matrix = generate_lower_triangular_matrix(5)
    print(matrix)
    


test_permute_feature_vector()
test_create_diagonal_matrix()
test_generate_lower_triangular_matrix()
test_multiply_matrices()