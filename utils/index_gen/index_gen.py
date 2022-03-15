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





