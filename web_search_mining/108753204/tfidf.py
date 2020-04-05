from __future__ import division, unicode_literals
import math, numpy as np
from textblob import TextBlob as tb

def tf(all_word, blob):
    return 0.5 + 0.5 * all_word/np.max(all_word)
    return np.log(1+all_word)
    # return all_word / len(blob)

def n_containing(all_word, bloblist):
    return np.array([sum(1 for blob in bloblist if word in blob) for word in all_word])

def idf(all_word, bloblist):
    return np.log(len(bloblist) / (1 + n_containing(all_word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
