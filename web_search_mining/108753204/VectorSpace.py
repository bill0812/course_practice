from pprint import pprint
from Parser import Parser
from tfidf import *
from util import *
import nltk
from textblob import TextBlob as tb

# teacher's original code, but modified some part
class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers. 
    A document is represented as a vector. Each dimension of the vector corresponds to a 
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """

    # Collection of document term vectors
    document_vectors = []

    # Mapping of vector index to keyword
    vector_keyword_index=[]

    # Tidies terms
    parser=None


    def __init__(self, documents=[], id=[]):
        self.document_vectors=[]
        self.all_id = id
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)
        
        # initialize all variables we need
        self.tf_vector = np.zeros((len(self.document_vectors), len(self.document_vectors[0])))
        self.raw_tf = np.zeros((len(self.document_vectors), len(self.document_vectors[0])))
        self.idf_vector, self.query_vector = None, None
        self.doc_tb_vector = list()

    def build(self,documents):
        """ Create the vector space for the passed document strings """
        self.vector_keyword_index = self.get_vector_index_from_keyword(documents)
        self.vector_index_keyword = self.get_vector_keyword_from_index()
        self.document_vectors = [self.make_vector(document) for document in documents]
    
    # get keyword index, lile {"test": "1"}
    def get_vector_index_from_keyword(self, document_list):
        """ create the keyword associated to the position of the elements within the document vectors """
        vocabulary_string = " ".join(document_list)
        vocabulary_list = self.parser.tokenise(vocabulary_string)
        vocabulary_list = self.parser.remove_stop_words(vocabulary_list)
        unique_vocabulary_list = remove_duplicates(vocabulary_list)
        vector_index={}
        offset=0
        for word in unique_vocabulary_list:
            vector_index[word]=offset
            offset+=1
        return vector_index
    
    # get index from keyword, like {"1":"test"}
    def get_vector_keyword_from_index(self):
        vector_index_keyword = dict()
        for word, index in self.vector_keyword_index.items():
            vector_index_keyword[index] = word
        return vector_index_keyword

    def make_vector(self, word_string):
        """ @pre: unique(vectorIndex) """
        vector = [0] * len(self.vector_keyword_index)
        word_list = self.parser.tokenise(word_string)
        word_list = self.parser.remove_stop_words(word_list)
        for word in word_list:
            vector[self.vector_keyword_index[word]] += 1
        return vector

    def build_query_vector(self, term_list):
        """ convert query string into a term vector """
        query = self.make_vector(" ".join(term_list))
        return query

    # get each doc's term frequency
    def get_tf_vector(self, all_content, tf_method):  
        for idx, each_doc in enumerate(all_content) :
            each_doc_tb = tb(each_doc).words
            self.raw_tf[idx] = self.document_vectors[idx]
            self.tf_vector[idx] = tf(self.raw_tf[idx], each_doc_tb, tf_method)
            self.doc_tb_vector.append(list(each_doc_tb))
        return self.tf_vector, self.raw_tf, self.doc_tb_vector

    # get idf vector from key index
    def get_idf_vector(self, idf_method):
        self.idf_vector = idf(self.vector_index_keyword.values(), self.raw_tf, idf_method)
        return self.idf_vector
 
    # get query vector
    def get_query_vector(self, query):
        self.query_vector = np.array(self.build_query_vector(query.split(' ')))
        return self.query_vector

    # use for feedback query, problem 5
    def feedback(self, final_result, query_vector, doc_vector, func):
        
        # get first id from problem three
        first_id = list(final_result.keys())[0]
        first_content = list()
        for index, word_count in enumerate(doc_vector[np.where(np.array(self.all_id) == first_id)[0][0]]):
            if word_count > 0 :
                word = self.vector_index_keyword[index]
                first_content.append(word)
        
        # get original feedback query
        pos_vector = [0] * len(self.tf_vector[0])
        for index, word in enumerate(first_content):
            tag = nltk.pos_tag([word])
            if tag[0][1] in ["NN", "VB"] and word in list(self.vector_keyword_index.keys()):
                word_id = self.vector_keyword_index[word]
                pos_vector[word_id] = doc_vector[np.where(np.array(self.all_id) == first_id)[0][0]][word_id]
    
        # get new query
        pos_vector = np.array(pos_vector)
        feedback_vector = np.einsum('i, i->i', pos_vector, self.idf_vector)
        new_query_vector = np.add(query_vector, np.multiply(0.5, feedback_vector))
        
        # get distance and map result
        each_dst = [func(new_query_vector, each_doc_vector) for each_doc_vector in doc_vector]
        mapped_result = dict(zip(list(self.all_id), list(each_dst)))
        
        # check reverse status
        if func.__name__ == "cosine":
            status = True
        else :
            status = False

        final_result = {k: v for k, v in sorted(mapped_result.items(), key=lambda item:item[1], reverse=status)}
        
        return final_result

    # print all distance one by one
    def get_print_distance(self, ALL_OPERATION) :

        # go through each problem
        for idx, (problems, method) in enumerate(ALL_OPERATION.items()):
            # initial 0 distance
            each_dst = 0

            # get final uery and get distance
            query_vector, doc_vector = get_final_vector(method[0], self.tf_vector, self.query_vector, self.idf_vector)     
            each_dst = [method[1](query_vector, each_doc_vector) for each_doc_vector in doc_vector]
        
            # map the result 
            mapped_result = dict(zip(list(self.all_id), list(each_dst)))
        
            # check reverse status
            if method[1].__name__ == "cosine":
                status = True
            else :
                status = False

            final_result = {k: v for k, v in sorted(mapped_result.items(), key=lambda item:item[1], reverse=status)}
        
            # if it's the last question, using feedback
            if idx == 4 :
                mapped_content = dict(zip(list(self.all_id),list(self.doc_tb_vector)))
                final_result = self.feedback(final_result, query_vector, doc_vector, method[1])
        
            # finally, print out score
            print("DocID    Score   {}".format(problems))
            for result_idx, (key, value) in enumerate(final_result.items()) :
                if result_idx == 5 :
                    break
                print("{}   {}   ".format(key, round(value, 6)))
            print("=======================")
