from trap_gen import extend_feature_vector, convert_sim_to_theta

def test_extend_feature_vector():

    feature_vec = [-4,6]
    beta = 1
    rq = 3
    theta = 2

    extended_vec = extend_feature_vector(feature_vec, beta,rq, theta)
    print(extended_vec)

def test_convert_sim_to_theta():

    sim = 1/3
    c = 1

    theta = convert_sim_to_theta(sim,c)
    print(theta)
    

test_extend_feature_vector()
test_convert_sim_to_theta()