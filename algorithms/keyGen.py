#for imports as runtime
import sys
sys.path.append("../utils/key_gen")

import key_gen as KG

def keyGen(key_size, dimension):

    kmg = KG.generate_hex_key(key_size)
    M1, M1_inv = KG.generate_random_non_singular_matrix(dimension)
    M2, M2_inv = KG.generate_random_non_singular_matrix(dimension)
    permut = KG.generate_random_permutation(dimension)

    #create result dictionary
    result = {}
    result["M1"] = M1
    result["M1_inv"] = M1_inv
    result["M2"] = M2
    result["M2_inv"] = M2_inv
    result["key"] = kmg

    return result


