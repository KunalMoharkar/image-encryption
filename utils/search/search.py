import numpy as np
import sys
sys.path.append("..")

from general_utils import multiply_matrices

def compute_matrix_trace(matrix):
    return np.trace(matrix)

#returns p matrix form index and trapdoor
def get_p_matrix(E,TD):

    return multiply_matrices([E,TD])

