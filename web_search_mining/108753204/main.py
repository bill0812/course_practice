# import basic packages
from glob import glob
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
import os, sys, time, pickle, numpy as np

# import other useful packages
from VectorSpace import VectorSpace
from tfidf import *
from util import *

# global variable
MODEL_PATH = "model.pickle"
DOC_DIR = "documents"
FILE_TYPE = "product"
ALL_OPERATION = {
        "Tearm Frequency (TF) Weighting + Cosine Similarity":["tf",cosine],
        "Term Frequency (TF) Weighting + Euclidean Distance":["tf",euclidean_dist],
        "TF-IDF Weighting + Cosine Similarity":["tfidf",cosine],
        "TF-IDF Weighting + Euclidean Distance":["tfidf",euclidean_dist],
        "Feedback Queries + TF-IDF Weighting + Cosine Similarity": ["tfidf", cosine]
}

# define all args we need
def get_args():
    parser = ArgumentParser('Project 1: Search and Rank via Vector Space Models.', formatter_class=RawTextHelpFormatter)
    parser.add_argument('--query', metavar="'some query'", required=True, dest="query", help="Enter your Query.")
    parser.add_argument("--tf", type=int, default=1, choices=[1,2,3], help="Choose tf method, \n1 for raw count.\n2 for term frequency.\n3 for log raw frequency.\nDefault is raw count")
    parser.add_argument("--idf", type=int, default=1, choices=[1,2,3], help="Choose idf method.\n1 for inverse document frequency.\n2 for inverse document frequency smooth.\n4 for Probabilistic inverse document frequency.\nDefault is inverse document frequnecy")
    return parser.parse_args()

# get all document, and sort them
# return all content, id and document count.
# Also, start counter
def get_all_doc(doc_path):
    print("Start Processing...")
    start = time.time()
    all_doc = sorted(glob(doc_path))
    print("Total document count: {}".format(len(all_doc)))
    all_content, all_id = list(), list()
    for index, doc_name in enumerate(all_doc):
        all_id.append(os.path.splitext(os.path.basename(doc_name))[0])
        with open(doc_name) as doc :
            all_content.append(doc.read())
    doc_count = len(all_content)
    return all_content, all_id, doc_count, start

# build svm model, return vector space model
def get_vsm(all_content, all_id):
    assert len(all_content) >= 1, "Document in the collection should be more than one"
    try:
        print('Try to load model......')
        with open(MODEL_PATH, 'rb') as reader:
            vector_space = pickle.load(reader)
        print("Model Found !")
    except FileNotFoundError:
        print('Model not found......')
        vector_space = VectorSpace(all_content, all_id)   
        with open(MODEL_PATH, 'wb') as writer:
            pickle.dump(vector_space, writer)
        print('Save built model......')

    return vector_space

if __name__ == "__main__":
    
    # get all variable and print out status
    args = get_args()
    query = args.query
    tf_method = args.tf
    idf_method = args.idf
    assert tf_method in [1,2,3] and idf_method in [1,2,3], "Wrong TF or IDF Method"
    
    # print info
    doc_path = os.path.join(DOC_DIR, "*."+FILE_TYPE)
    print("Using Query: {}".format(query))
    print("Processing: {}".format(doc_path))
    print("====================================")
    
    # get all docs
    all_content, all_id, doc_count, start = get_all_doc(doc_path)
    
    # get vectorspace mode and its data
    vector_space  = get_vsm(all_content, all_id)
    
    # get tf vector
    tf_vector, raw_tf, doc_tb_vector = vector_space.get_tf_vector(all_content, tf_method)
    
    # count each doc's idf
    idf_vector = vector_space.get_idf_vector(idf_method)
    
    # here for query indexing
    query_vector = vector_space.get_query_vector(query)
    
    # print result
    vector_space.get_print_distance(ALL_OPERATION) 

    # retrieve spending time
    end = time.time()
    print(round(end - start, 2), "Seconds")
