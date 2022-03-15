from index_gen import extend_feature_vector

def test_extend_feature_vector():

    feature_vec = [1,2,3,4,2]
    alpha = 2
    rf = 3

    extended_vec = extend_feature_vector(feature_vec,alpha,rf)
    print(extended_vec)

