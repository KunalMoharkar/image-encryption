from keyGen import keyGen, storeKeyToFile, readKeyFromFile

def test_keyGen():

    result = keyGen(80,2)
    print(result)

def test_storeKeyToFile():

    result = keyGen(80,2)
    storeKeyToFile(result)

def test_readKeyFromFile():

    result =  readKeyFromFile()
    print(result)


#test_keyGen()
test_storeKeyToFile()
test_readKeyFromFile()