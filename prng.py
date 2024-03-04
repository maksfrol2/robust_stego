import random
import numpy as np

def gen_rand_string(m,seed):
    random.seed(seed)
    randomlist = []
    for i in range(m):
        n = random.random()
        randomlist.append(n)
    return randomlist 

def gen_pos_seq(q):
    q_sort = np.argsort(q)

    return q_sort