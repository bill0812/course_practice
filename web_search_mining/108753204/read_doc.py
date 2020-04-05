# import basic packages
from glob import glob
from argparse import ArgumentParser
from textblob import TextBlob as tb
import os, sys, time, numpy as np
import nltk

# import other useful packages
from VectorSpace import VectorSpace
from tfidf_np import *
from util import *

# global variable
DOC_DIR = "documents"
FILE_TYPE = "product"
TYEPS = [
        "Term Frequency (TF) Weighting + Cosine Similarity",
        "Term Frequency (TF) Weighting + Euclidean Distance",
        "TF-IDF Weighting + Cosine Similarity",
        "TF-IDF Weighting + Euclidean Distance",
        "Feedback Queries + TF-IDF Weighting + Cosine Similarity"
        ]

def get_args():
    parser = ArgumentParser('Project 1: Search and Rank via Vector Space Models.')
    parser.add_argument('--query', required=True, dest="query", help="Enter your Query.")
    parser.add_argument('--fb', action="store_true", help="Use it for feedback option")
    return parser.parse_args()

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

def get_vsm(all_content):
    vector_space = VectorSpace(all_content)   
    assert len(vector_space.document_vectors) >= 1
    tf_vector = np.zeros((doc_count, len(vector_space.document_vectors[0])))
    doc_vector = np.asarray(vector_space.document_vectors)
    key_word_index = vector_space.vector_keyword_index
    index_key_word = vector_space.vector_index_keyword
    doc_tb_vector = list()
    return tf_vector, doc_vector, key_word_index, index_key_word, vector_space, doc_tb_vector

def get_tf_vector(all_content, tf_vector, doc_vector, key_word_index, doc_tb_vector): 
    for idx, each_doc in enumerate(all_content) :
        each_doc_tb = tb(each_doc).words
        each_doc_vector = doc_vector[idx]
        tf_vector[idx] = each_doc_vector
        # tf_vector[idx] = tf(each_doc_vector, each_doc_tb)
        doc_tb_vector.append(list(each_doc_tb))
    return tf_vector, doc_tb_vector

def get_idf_vector(doc_count, index_key_word, doc_tb_vector, all_content):
    idf_vector = idf(index_key_word.values(), doc_tb_vector)
    return idf_vector

def get_query_vector(query,vector_space):
    query_vector = np.array(vector_space.build_query_vector(query.split(' ')))
    return query_vector

def get_final_vector(tf_vector, idf_vector, query_vector):
    final_query_tf = query_vector
    final_tf_vector = tf_vector
    idf_vector_original = idf_vector
    final_query_tfidf = np.einsum('i, i->i', query_vector, idf_vector)
    idf_vector.shape = (1, len(idf_vector))
    final_tfidf_vector = np.einsum('ij, ij->ij', tf_vector, idf_vector)
    return final_tf_vector, final_tfidf_vector, final_query_tf, final_query_tfidf, idf_vector

def check_feedback(final_result, all_id, mapped_content, data, idf_vector, key_word_index):
    first_id = list(final_result.keys())[0]
    fisrt_content = mapped_content[first_id]
    pos_vector = [0] * len(idf_vector[0])
    for index, word in enumerate(fisrt_content):
        tag = nltk.pos_tag(word)
        if tag in ["NN", "VB"] and tag in key_word_index.keys():
            word_id = key_word_index[tag]
            pos_vector[word_id] += 1
    pos_vector = np.array(pos_vector)
    print(idf_vector.shape)
    idf_vector.shape = (len(idf_vector[0]),) 
    feedback_vector = np.einsum('i, i->i', pos_vector, idf_vector)
    new_query_vector = np.add(data[1], np.multiply(0.5, feedback_vector))
    each_dst = [cosine(new_query_vector, each_doc_vector) for each_doc_vector in data[0]]
    mapped_result = dict(zip(list(all_id), list(each_dst)))
    final_result = {k: v for k, v in sorted(mapped_result.items(), key=lambda item:item[1], reverse=True)}
    return final_result

def get_print_distance(final_tf_vector, final_tfidf_vector, final_query_tf, final_query_tfidf, feedback, all_content, idf_vector, key_word_index):
    all_operation = {
                "1" : [final_tf_vector, final_query_tf],
                "2" : [final_tf_vector, final_query_tf],
                "3" : [final_tfidf_vector, final_query_tfidf],
                "4" : [final_tfidf_vector, final_query_tfidf],
                "5" : [final_tfidf_vector, final_query_tfidf]
            }
    for idx, (each_kind, data) in enumerate(all_operation.items()):
        each_dst = 0
        if idx%2 == 0:
            each_dst = [cosine(data[1], each_doc_vector) for each_doc_vector in data[0]]
        else :
            each_dst = [euclidean_dist(data[1], each_doc_vector) for each_doc_vector in data[0]]
        mapped_result = dict(zip(list(all_id), list(each_dst)))
        if idx%2 == 0 :
            final_result = {k: v for k, v in sorted(mapped_result.items(), key=lambda item:item[1], reverse=True)}
        else :
            final_result = {k: v for k, v in sorted(mapped_result.items(), key=lambda item:item[1], reverse=False)}    
        if each_kind == "5" and feedback:
            mapped_content = dict(zip(list(all_id),list(all_content)))
            final_result = check_feedback(final_result, all_id, mapped_content, data, idf_vector, key_word_index)
    
        print("DocID    Score   {}".format(TYEPS[idx]))
        for result_idx, (key, value) in enumerate(final_result.items()) :
            if result_idx == 5 :
                break
            print("{}   {}   ".format(key, round(value, 6)))
        print("=======================")

if __name__ == "__main__":
    
    args = get_args()
    query = args.query
    feedback = args.fb
    doc_path = os.path.join(DOC_DIR, "*."+FILE_TYPE)
    print("Using Query: {}".format(query))
    print("Processing: {}".format(doc_path))
    print("Feedback or not: {}".format(feedback))
    print("====================================")
    
    # get all docs
    all_content, all_id, doc_count, start = get_all_doc(doc_path)
    
    # get vectorspace mode and its data
    tf_vector, doc_vector, key_word_index, index_key_word, vector_space, doc_tb_vector  = get_vsm(all_content)

    # get tf vector
    tf_vector, doc_tb_vector = get_tf_vector(all_content, tf_vector, doc_vector, key_word_index, doc_tb_vector)
    
    # count each doc's idf
    idf_vector = get_idf_vector(doc_count, index_key_word, doc_tb_vector, all_content)

    # here for query indexing
    query_vector = get_query_vector(query, vector_space)
    
    # get final query and weighting
    final_tf_vector, final_tfidf_vector, final_query_tf, final_query_tfidf, idf_vector = get_final_vector(tf_vector, idf_vector, query_vector)
    
    # calculate distance
    get_print_distance(final_tf_vector, final_tfidf_vector, final_query_tf, final_query_tfidf, feedback, all_content, idf_vector, key_word_index)
    
    # retrieve spending time
    end = time.time()
    print(round(end - start, 2), "Seconds")