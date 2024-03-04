import numpy as np
import random
import string
import math
from scipy.fftpack import dct, idct
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage import data, img_as_ubyte
from skimage import metrics as mt
import matplotlib.pylab as plt
import prng as rng
import test as mtr


def gen_seq_test(q1):
    q1_sort = np.argsort(q1)
    q1_sort += 1

    return q1_sort

def toBinary(a):
    m = ''.join(format(ord(i), '08b') for i in a)
    return m

def toString(a):
    m = "".join(chr(int(a[i:i+8], 2)) for i in range(0, len(a), 8))
    return m

def gen_rand_string(m):
    randomlist = []
    for i in range(m):
        n = random.random()
        randomlist.append(n)
    return randomlist

def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def Encode (img_path, msg, l,seed1,seed2,seed3):
    im = rgb2gray(imread(img_path))
    #im = (imread(img_path))
    bin = toBinary(msg)

    q1 = rng.gen_pos_seq(rng.gen_rand_string(im.shape[0],seed1))
    q2 = rng.gen_pos_seq(rng.gen_rand_string((im.shape[1] - l),seed2))
    c3 = rng.gen_rand_string(len(bin),seed3)

    imF = dct2(im)
    count = 0
    print(len(bin))
    for i in bin:
        if int(i) == 1:
             #print(q2[count] + l)
             #print('q1 = ',q1[count])
             imF[q1[count]][q2[count] + l] = c3[count]
        if count != len(bin):
            count += 1
            print(count)
    
    im1 = idct2(imF)
    imsave('encoded.tif', im1)

    return im1

def Decode (img_path, l, seed1,seed2,seed3,length):
    bin =''
    im = imread(img_path)
    imF = dct2(im)
    
    q1 = rng.gen_pos_seq(rng.gen_rand_string(im.shape[0],seed1))
    q2 = rng.gen_pos_seq(rng.gen_rand_string((im.shape[1] - 50),seed2))
    c3 = rng.gen_rand_string(length * 8,seed3)   

    count = 0
    while count < len(c3):
        if round(imF[q1[count]][q2[count] + l],2) == round(c3[count],2):
            bin += '1'
        else:
            bin += '0'
        
        count += 1

    msg = toString(bin)
    return msg

message = 'Lorem ipsum dolor sit amet cras.'
Encode('baboon.jpg',message,50,423,2345,2345)
print(Decode('encoded.tif',50,570,8301,4839,len(message)))
print(mtr.get_metrics('baboon.jpg','encoded.tif'))