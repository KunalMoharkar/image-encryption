import numpy as np

def extend_feature_vector(featureVec, beta, rq, theta):
    
    assert beta >= 0
    #contanins values to to appended at the end of vector
    new_values = [] 
    #compute sq. sum
    sq_sum = 0
    for value in featureVec:
        sq_sum += value*value

    new_values.append(-beta*sq_sum)
    new_values.append(beta)
    #beta*theta^2
    new_values.append(beta*theta*theta)
    new_values.append(rq)
    new_values.append(0)
    
    new_feature_vec = 2*beta*np.array(featureVec)
    #extended vector after appendin new values
    extended_feature_vec = list(new_feature_vec) + new_values

    return extended_feature_vec

def convert_sim_to_theta(sim,c):

    theta = (c-sim)/sim
    #round off till 2 decimals
    theta = round(theta,2)
    return theta

