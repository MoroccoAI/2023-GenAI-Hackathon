import fitz
import re
import numpy as np
import random
import os

all_ce = []
chks = []

def cosim(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

## compute similarities
def get_rel(qe, top_n=1):
    sims = []
    for ce in all_ce:
        sim = cosim(qe, ce)
        sims.append(sim)
        
    ids = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)[:top_n]
    rel_parts = []
    for i in ids:
        rel_parts.append(chks[i])
        
    rel_parts = '\n'.join(rel_parts)
    
    return rel_parts  #, ids

def make_pmt(rel_parts, qst):
    p = "given the following text: \n" + rel_parts + "\n\nAnswer the following query: " + qst + "\ngive the answer followed by the page number as \
    [ Page Number] notation and stop point. Note: every result has this number at the beginning. Also, if the query says: see value 2, it means you should consider the one afterward. if it says value 3, it's the one after afterward, and so on."

    return p