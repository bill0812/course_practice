from pprint import pprint
from Parser import Parser
import util

class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers. 
    A document is represented as a vector. Each dimension of the vector corresponds to a 
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """

    #Collection of document term vectors
    document_vectors = []

    #Mapping of vector index to keyword
    vector_keyword_index=[]

    #Tidies terms
    parser=None


    def __init__(self, documents=[]):
        self.document_vectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)

    def build(self,documents):
        """ Create the vector space for the passed document strings """
        self.vector_keyword_index = self.get_vector_keyword_index(documents)
        self.vector_index_keyword = self.get_vector_keyword_from_index()
        self.document_vectors = [self.make_vector(document) for document in documents]

    def get_vector_keyword_index(self, document_list):
        """ create the keyword associated to the position of the elements within the document vectors """
        vocabulary_string = " ".join(document_list)
        vocabulary_list = self.parser.tokenise(vocabulary_string)
        vocabulary_list = self.parser.remove_stop_words(vocabulary_list)
        unique_vocabulary_list = util.remove_duplicates(vocabulary_list)
        vector_index={}
        offset=0
        for word in unique_vocabulary_list:
            vector_index[word]=offset
            offset+=1
        return vector_index

    def get_vector_keyword_from_index(self):
        vectorIndexKeyword = dict()
        for word, index in self.vector_keyword_index.items():
            vectorIndexKeyword[index] = word
        return vectorIndexKeyword


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
