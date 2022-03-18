from key_gen import generate_hex_key, generate_random_permutation, generate_random_non_singular_matrix

def test_generate_hex_key():

    key = generate_hex_key(80)
    print(key)

def test_generate_random_permutation():

    permut = generate_random_permutation(2)
    print(permut)

def test_generate_random_non_singular_matrix():

    M1, M1_inv = generate_random_non_singular_matrix(2)
    
    M2, M2_inv = generate_random_non_singular_matrix(2)

test_generate_random_permutation()
test_generate_hex_key()
test_generate_random_non_singular_matrix()
