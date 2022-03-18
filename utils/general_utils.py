import decimal
import numpy as np

#accepts list of matrices as input and returns the result
def multiply_matrices(matrices):
    #initial result matrix is I
    n = len(matrices[0])
    result = np.identity(n, dtype = float)
    
    for matrix in matrices:
        result = np.matmul(result, matrix)

    #round off to 5 decimal values
    return result.round(decimals = 5)

def permute_feature_vector(feature_vector, permutation):

    new_feature_vector = []
    #perform permutation
    for value in permutation:
        index = value-1
        new_feature_vector.append(feature_vector[index])

    return new_feature_vector

def create_diagonal_matrix(feature_vector):

    diagonal_elements = np.array(feature_vector)
    return np.diag(diagonal_elements).astype('float')

def generate_lower_triangular_matrix(dimension):
    #generate a random n*n matrix
    n = dimension
    matrix = np.random.rand(n,n)
    #lower_triangular_matrix
    lt_matrix = np.tril(matrix)
    #make diagonal elements 1
    np.fill_diagonal(lt_matrix, 1)
    
    return lt_matrix


