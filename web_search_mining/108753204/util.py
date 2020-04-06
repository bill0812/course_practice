import sys, os
import numpy as np

# teacher's original code, use in VectorSpace model
def remove_duplicates(list):
    """ remove duplicates from a list """
    return set((item for item in list))

# calculate cosine for each pairwise vector
def cosine(vector1, vector2):
    """ cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
    return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))

# calculate euclidean distance for each pairwise vector
def euclidean_dist(vector1, vector2):
    return np.linalg.norm(vector1-vector2)

# check the input argument from command line is diretory
def dir_path(input_string):
    if os.path.isdir(input_string):
        return input_string
    else:
        raise NotADirectoryError(input_string)

def get_final_vector(method, tf_vector, query_vector, idf_vector):
    
    if method == "tf" :
        return query_vector, tf_vector
    elif method == "tfidf" :
        idf_vector_cp = idf_vector.copy()
        query_vector = np.einsum('i, i->i', query_vector, idf_vector_cp)
        idf_vector_cp.shape = (1, len(idf_vector_cp))
        doc_vector = np.einsum('ij, ij->ij', tf_vector, idf_vector_cp)

        return query_vector, doc_vector
