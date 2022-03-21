import json
import sys
import random
from tqdm import tqdm

sys.path.append("../utils/index_gen")
sys.path.append("../utils")
import index_gen as IG
import general_utils as util

from keyGen import readKeyFromFile


def indexGen(feature_vec, key):

    dimension = len(feature_vec)
    M1 = key["M1"]
    M2 = key["M2"]
    permutation = key["permutation"]
    #choose randm num between 1-100.
    alpha = random.randint(1,100)
    rf = random.randint(1,100)

    ext_feature_vec = IG.extend_feature_vector(feature_vec,alpha,rf)
    permuted_fv = util.permute_feature_vector(ext_feature_vec, permutation)

    F = util.create_diagonal_matrix(permuted_fv)
    S = util.generate_lower_triangular_matrix(dimension)

    E = util.multiply_matrices([M1,S,F,M2])

    return E

def readFeatures(filename):

    filename = f"../data/Features/{filename}"
    features = []

    with open(filename, 'r') as fp:
        for line in fp: 
            row = json.loads(line) 
            features.append(row) 

    return features

def createIndex(features,key):

    results = []

    for feature in tqdm(features):

        temp = {}
        id = feature["id"]
        feature_vec = feature["feature_vec"]

        E = indexGen(feature_vec, key)

        temp["id"] = id
        temp["E"] = E.tolist()

        results.append(temp)

    return results

def storeIndexToFile(index_list, filename="index.jsonl"):

    for index in tqdm(index_list):
        json_object = json.dumps(index)
        with open(filename, "a") as outfile:
            outfile.write(json_object)
            outfile.write('\n')


if __name__ == "__main__":

    print("Reading Key from file ...")
    key = readKeyFromFile()
    print("Reading Features from file ...")
    features = readFeatures("features_32-2000.jsonl")
    print(f"Total images: {len(features)}, dimension : {len(features[0]['feature_vec'])}")
    print("Creating index ...")
    index_list = createIndex(features, key)
    print("Storing index to file ...")
    storeIndexToFile(index_list)
