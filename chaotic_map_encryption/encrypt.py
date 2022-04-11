import cv2
import sys
import random
import copy

sys.path.append("utils")

from utils import util
from utils import chaotic_maps as CM 

BLOCK_SIZE = 16

def get_image_block(img, block_no):

    h,w = img.shape[0], img.shape[1]
    start = block_no*BLOCK_SIZE
    row = start//h
    
    col_start = (block_no%2)*BLOCK_SIZE
    col_end = col_start + BLOCK_SIZE
    
    pix = []

    for i in range(col_start, col_end):
        pix.append([img[row][i][0],img[row][i][1],img[row][i][2]])

    return pix

def read_image(path):
    
    img = cv2.imread(path)
    return img

def chaotic_map_enc(img,key):
    
    enc_image = copy.deepcopy(img)
    h,w = img.shape[0], img.shape[1]
    num_blocks = img.shape[0]*img.shape[0]//BLOCK_SIZE
    dec_key = CM.generate_decimal_kmg(key)

    #for each block
    for i in range(num_blocks):

        block = get_image_block(img,i)
        start = i*BLOCK_SIZE
        row = start//h
        col_start = (i%2)*BLOCK_SIZE
        
        for image_bit in block:
           
           num_steps = dec_key[9]

           y_vals = CM.iterate_y0(num_steps,0.3)
           for k in range(num_steps):
            
            val = y_vals[k]

            op = util.get_operation_to_perform(val)
        
            if op == 1:
                res = util.not_operation(image_bit)
            elif op==2:
                res = util.xor_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]))
            elif op==3:
                res = util.modulo_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]))
            elif op==4:
                res = util.xor_not_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]))
            elif op==5:
                res = util.xor_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]))
            elif op==6:
                res = util.modulo_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]))
            elif op==7:
                res = util.xor_not_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]))                     
            else:
                res = (image_bit[0],image_bit[1],image_bit[2])      
            
                   
             
            image_bit[0],image_bit[1],image_bit[2] = res[0], res[1], res[2]
            
        
           r,g,b = res[0],res[1],res[2]
           
           enc_image[row][col_start][0] = r
           enc_image[row][col_start][1] = g
           enc_image[row][col_start][2] = b

           col_start += 1
        
    return enc_image

def chaotic_map_dec(img,key):
    
    enc_image = copy.deepcopy(img)
    h,w = img.shape[0], img.shape[1]
    num_blocks = img.shape[0]*img.shape[0]//BLOCK_SIZE
    dec_key = CM.generate_decimal_kmg(key)

    #for each block
    for i in range(num_blocks):

        block = get_image_block(img,i)
        start = i*BLOCK_SIZE
        row = start//h
        col_start = (i%2)*BLOCK_SIZE
        
        for image_bit in block:
           
           num_steps = dec_key[9]

           y_vals = CM.iterate_y0(num_steps,0.3)
          
           #reverse for decryption
           y_vals = y_vals[::-1]
           for val in y_vals:
            
            op = util.get_operation_to_perform(val)
        
            if op == 1:
                res = util.not_operation(image_bit)
            elif op==2:
                res = util.xor_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]))
            elif op==3:
                res = util.modulo_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]),mode="dec")
            elif op==4:
                res = util.xor_not_operation(image_bit,(dec_key[3],dec_key[4],dec_key[5]),mode="dec")
            elif op==5:
                res = util.xor_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]))
            elif op==6:
                res = util.modulo_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]),mode="dec") 
            elif op==7:
                res = util.xor_not_operation(image_bit,(dec_key[6],dec_key[7],dec_key[8]),mode="dec")        
            else:
                res = (image_bit[0],image_bit[1],image_bit[2])  
            
        
            image_bit[0],image_bit[1],image_bit[2] = res[0], res[1], res[2]
        
           r,g,b = res[0],res[1],res[2]
           
           enc_image[row][col_start][0] = r
           enc_image[row][col_start][1] = g
           enc_image[row][col_start][2] = b

           col_start += 1
        
    return enc_image


img = read_image("E:/NTMC/data/CIFAR-10/bird-1000/109.png")
enc_img = chaotic_map_enc(img,"ABCDEABCDEABCDEABCA4")
dec_img = chaotic_map_dec(enc_img,"ABCDEABCDEABCDEABCA4")

print((img == dec_img).all())