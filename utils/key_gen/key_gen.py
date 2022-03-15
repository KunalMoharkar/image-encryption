import random
#generate a random hexadec key with input bits size
def generate_hex_key(size):

    #1 hex = 4 bits
    num_chars = size//4
    hex_chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    assert len(hex_chars) == 16

    key = ""
    for i in range(num_chars):
        key+= random.choice(hex_chars)[0]

    return key

def generate_random_permutation(dimension):

    #permuation mappoing l+5 -> l+5
    n = dimension + 5
    permutation = []

    for i in range(1,n+1):

        permutation.append(i)

    random.shuffle(permutation)

    return permutation



