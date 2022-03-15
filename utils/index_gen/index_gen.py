import numpy as np

def extend_feature_vector(featureVec, alpha, rf):
    
    assert alpha >= 0
    #contanins values to to appended at the end of vector
    new_values = [] 
    #compute sq. sum
    sq_sum = 0
    for value in featureVec:
        sq_sum += value*value

    new_values.append(alpha)
    new_values.append(-alpha*sq_sum)
    new_values.append(alpha)
    new_values.append(0)
    new_values.append(rf)

    new_feature_vec = alpha*np.array(featureVec)
    #extended vector after appendin new values
    extended_feature_vec = list(new_feature_vec) + new_values

    return extended_feature_vec

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






