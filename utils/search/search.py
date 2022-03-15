import numpy as np

#accepts list of matrices as input and returns the result
def multiply_matrices(matrices):
    #initial result matrix is I
    n = len(matrices[0])
    result = np.identity(n, dtype = float)
    
    for matrix in matrices:
        result = np.matmul(result, matrix)

    return result

def compute_matrix_trace(matrix):
    return np.trace(matrix)

#returns p matrix form index and trapdoor
def get_p_matrix(E,TD):

    return multiply_matrices([E,TD])

