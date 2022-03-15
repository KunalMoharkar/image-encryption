from index_gen import extend_feature_vector, permute_feature_vector, create_diagonal_matrix, generate_lower_triangular_matrix

def test_extend_feature_vector():

    feature_vec = [1,2,3,4,2]
    alpha = 2
    rf = 3

    extended_vec = extend_feature_vector(feature_vec,alpha,rf)
    print(extended_vec)

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
    


test_extend_feature_vector()
test_permute_feature_vector()
test_create_diagonal_matrix()
test_generate_lower_triangular_matrix()