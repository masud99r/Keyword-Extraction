from __future__ import absolute_import
from __future__ import print_function
import six
__author__ = 'a_medelyan'

import rake
import operator
import io

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
#def __init__(self, stop_words_path, min_char_length=1, max_words_length=5, min_keyword_frequency=1):

rake_object = rake.Rake(stoppath, 1, 3, 1)

# 2. run on RAKE on a given text
sample_file = io.open("preprocessdata/cluster.txt", 'r',encoding="iso-8859-1")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)

print("----------")
