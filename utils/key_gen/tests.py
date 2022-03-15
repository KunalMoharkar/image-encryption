from key_gen import generate_hex_key, generate_random_permutation

def test_generate_hex_key():

    key = generate_hex_key(80)
    print(key)

def test_generate_random_permutation():

    permut = generate_random_permutation(2)
    print(permut)

test_generate_random_permutation()
test_generate_hex_key()

