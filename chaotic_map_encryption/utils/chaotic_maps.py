import random
import math

CHAOTIC_MAP_CONSTANT = 3.9999

def generate_decimal_kmg(kmg):

    i = 0

    kmg_asc = []

    for i in range(0,20,2):

        temp = kmg[i]
        temp += kmg[i+1]

        temp_num = int(temp,16)

        #print(temp_num)
        kmg_asc.append(temp_num)
    
    return kmg_asc

    


def generate_xo1(K4, K5, K6):

    K4_bin = '{:08b}'.format(K4)

    K5_bin = '{:08b}'.format(K5)

    K6_bin = '{:08b}'.format(K6)

    i = 0

    x01_num = 0

    for j in range(8):

        num = int(K4_bin[j])
        #print(num)
        temp = num * pow(2, i)
        x01_num += temp
        i = i+1
    
    #print(x01_num)
    
    for j in range(8):

        num = int(K5_bin[j])
        #print(num)
        temp = num * pow(2, i)
        x01_num += temp
        i = i+1
    
    #print(x01_num)

    for j in range(8):

        num = int(K6_bin[j])
        #print(num)
        temp = num * pow(2, i)
        x01_num += temp
        i = i+1
    
    #print(x01_num)

    x01_den = pow(2, 24)

    x01 = x01_num/x01_den

    #print(x01)

    return x01


def generate_x02():

    x02_num = 0

    for i in range(12,18):

        num = int(kmg[i], 16)
        #print(num)
        x02_num += num

    x02 = x02_num/96
    #print(x02)
    return x02


def generate_xo(kmg_asc):

    x01 = generate_xo1(kmg_asc[3], kmg_asc[4], kmg_asc[5])

    x02 = generate_x02()

    x0 = (x01 + x02)%1

    print(x0)

    return x0


def iterate_y0(num_values,y0):

    generated_vals = 0
    y_vals = []

    while(generated_vals < num_values):
        
        y = CHAOTIC_MAP_CONSTANT*y0*(1-y0)
        y0 = y

        if y >=0.1 and y<=0.9:
    
            y_vals.append(round(y,2))
            generated_vals+=1

    return y_vals






    



