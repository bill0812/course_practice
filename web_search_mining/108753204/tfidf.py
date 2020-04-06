from __future__ import division, unicode_literals
import math, numpy as np
from textblob import TextBlob as t2

# different method of tf
def tf(raw_tf, blob, method):

    if method == 1 :
        return raw_tf
    elif method == 2 :
        return raw_tf / len(blob)
    else :
        return np.log(1+raw_tf)

# calculate 'n_containing' in one line 
def n_containing(all_word, all_tf):
    count_index = np.zeros((len(all_tf[0])))
    for each_doc in all_tf :
        for index, count in enumerate(each_doc):
            if count > 0 :
                count_index[index] += 1
    return count_index

# calculate different method of idf
def idf(all_word, all_tf, method):
    if method == 1 :
        return np.log(len(all_tf) / (n_containing(all_word, all_tf)))
    elif method == 2 :
        return 1 + np.log(len(all_tf) / (1 + n_containing(all_word, all_tf)))
    else :
        n = n_containing(all_word, all_tf)
        return np.log(len(all_tf)-n / n)

