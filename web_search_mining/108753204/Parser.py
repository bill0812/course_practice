#http://tartarus.org/~martin/PorterStemmer/python.txt
from PorterStemmer import PorterStemmer

class Parser:
    stemmer=None
    stopwords=[]
    def __init__(self,):
        self.stemmer = PorterStemmer()
        self.stopwords = open('english.stop', 'r').read().split()

    def clean(self, string):
        """ remove any nasty grammar tokens from string """
        string = string.replace(".","")
        string = string.replace("\s+"," ")
        string = string.lower()
        return string

    def remove_stop_words(self,list):
        """ Remove common words which have no search value """
        return [word for word in list if word not in self.stopwords ]

    def tokenise(self, string):
        """ break string up into tokens and stem words """
        string = self.clean(string)
        words = string.split(" ")
        return [self.stemmer.stem(word,0,len(word)-1) for word in words]
