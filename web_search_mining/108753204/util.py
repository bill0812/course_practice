import sys, os
import numpy as np

def remove_duplicates(list):
    """ remove duplicates from a list """
    return set((item for item in list))

def cosine(vector1, vector2):
    """ cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
    return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

def euclidean_dist(vector1, vector2):
    return np.linalg.norm(vector1-vector2)

def dir_path(input_string):
    if os.path.isdir(input_string):
        return input_string
    else:
        raise NotADirectoryError(input_string)
