#for imports as runtime
import sys
import json
import numpy as np

sys.path.append("../utils/key_gen")
import key_gen as KG


NP_KEYS = ["M1","M1_inv","M2","M2_inv"]

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
    result["permutation"] = permut
    result["key"] = kmg

    return result

def storeKeyToFile(key):

    for dict_key in NP_KEYS:
        key[dict_key] = key[dict_key].tolist()
   
    json_object = json.dumps(key)
    with open("key.json", "w") as outfile:
        outfile.write(json_object)
        outfile.write('\n')

def readKeyFromFile(filename="key.json"):

    with open(filename, 'r') as fp:
        for line in fp: 
            key = json.loads(line)  

    for dict_key in NP_KEYS:
        key[dict_key] = np.array(key[dict_key], dtype='float')
    
    return key


if __name__ == "__main__":

    #system args
    keysize = int(sys.argv[1])
    dimension = int(sys.argv[2])

    print("Generating Key ... ")
    key = keyGen(keysize, dimension)
    print("Storing key to file key.json ... ")
    storeKeyToFile(key)