import collections
import os
import pickle
import re

import numpy as np
import pandas as pd

from nltk.tokenize import word_tokenize

TRAIN_DATA = "train_data.csv"
TEST_DATA = "test_data.csv"


def clean_str(text):
    text = re.sub(r"[^A-Za-z0-9(),!?\'\`\"]", " ", text)  #  去除特殊字符
    
