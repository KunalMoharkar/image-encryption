
def not_operation(image_bits):

    bin_vals = []
    #get 8 bit binary rerpesentation
    for bit in image_bits:
        
        #invert bits
        bit = 255 - bit
        bin_vals.append(bit)

    return bin_vals

def xor_operation(image_bits, key_bits):

    result = []
    for i in range(len(image_bits)):

        res = image_bits[i]^key_bits[i]
        result.append(res)

    #print(result)
    return result

def modulo_operation(image_bits, key_bits, mode="enc"):

    k4 = key_bits[0]
    k5 = key_bits[1]
    k6 = key_bits[2]
    r = image_bits[0]
    g = image_bits[1]
    b = image_bits[2]

    if mode == "enc":

        res1 = (r + k4 + k5)%256
        res2 = (g + k6 + k5)%256
        res3 = (b + k4 + k6)%256
    else:

        res1 = (r + 256 - k4 - k5)
        res2 = (g + 256 - k6 - k5)
        res3 = (b + 256 - k4 - k6)

    return [res1, res2, res3]
    
def xor_not_operation(image_bits, key_bits, mode="enc"):

    results = []

    for i in range(len(image_bits)):

        pix = image_bits[i]
        key = key_bits[i]

        if mode == "enc":
            #xor
            xor_res = pix^key
            #not
            res = 255 - xor_res
        else:
            #not
            pix = 255-pix
            #xor
            res = pix^key

        results.append(res)

    #print(results)
    return results

def get_operation_to_perform(val):

    #generate intervals
    start = 0.10
    intervals = [(start,0.03,1)]
    i = 2
    while(start < 0.55):

        group = i%8
        if group == 0:
            group = 8

        intervals.append((start+0.03,0.03,group))
        start+=0.03
        start = round(start,2)
        i+=1

    start = 0.58
    while(start < 0.9):
        group = i%8
        if group == 0:
            group = 8
        intervals.append((start,0.04,group))
        start+=0.04
        start = round(start,2)
        i+=1
    
    #print(intervals)
    for obj in intervals:

        start = obj[0]
        end = start + obj[1]
    
        if val >= start and val < end:

            return obj[2]



'''
not_operation((255,0,22))
xor_operation((0,255,3),(255,0,2))
print(modulo_operation((1,255,3),(255,12,2)))
print(modulo_operation((12,13,4),(255,12,2), mode="dec"))
xor_not_operation((12,13,4),(255,12,2), mode="enc")
xor_not_operation((12,254,249),(255,12,2), mode="dec")
op = get_operation_to_perform(0.63)
print(op)
'''