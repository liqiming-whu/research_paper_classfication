import collections
import os
import pickle
import re

import pandas as pd

from nltk.tokenize import word_tokenize

TRAIN_DATA = "train_data.csv"
TEST_DATA = "test_data.csv"


def clean_str(text):  # 清理
    text = re.sub(r"[^A-Za-z0-9(),!?\'\`\"]", " ", text)  # 去除特殊字符
    text = re.sub(r"\s{2,}", " ", text)  # 去除长空格
    text = text.strip().lower()  # 去除行首尾\t,\s,\n

    return text


def build_word_dict():  # 建立词表
    if not os.path.exists("word_dict.pickle"):
        train_df = pd.read_csv(TRAIN_DATA, names=["title", "content", "class"])
        contents = train_df["content"]

        words = list()
        for content in contents:
            for word in word_tokenize(clean_str(content)):
                words.append(word)

        word_counter = collections.Counter(words).most_common()  # 依据训练集建立词频字典
        word_dict = dict()
        word_dict["<pad>"] = 0   # 用于句子拓展
        word_dict["<unk>"] = 1   # 用于去除不在字典中的词，用1表示
        word_dict["<eos>"] = 2   # 结束符
        for word, _ in word_counter:
            word_dict[word] = len(word_dict)  # one-hot

        with open("word_dict.pikle", "wb") as f:
            pickle.dump(word_dict, f)

    else:
        with open("word_dict.pikle", "rb") as f:
            word_dict = pickle.load(f)

    return word_dict


def build_svm_dataset(step, word_dict):  # 创建数据集
    if step == "train":
        df = pd.read_csv(TRAIN_DATA, names=["title", "content", "class"])
    else:
        df = pd.read_csv(TEST_DATA, names=["title", "content", "class"])

    df = df.sample(frac=1)  # 打乱顺序
    x = list(map(lambda d: word_tokenize(clean_str(d)), df["content"]))
    x = list(map(lambda d: list(
        map(lambda w: word_dict.get(w, word_dict["<unk>"]), d)), x))
    x = list(map(lambda d: d + [word_dict["<eos>"]], x))

    y = list(map(lambda d: d - 1, list(df["class"])))

    return x, y


def addwhitespace(text):  # CountVectorizer().fit_transform()要求输入的每个字符以空格隔开，加上空格
    c = list()
    for i in text:
        a = map(str, i)
        b = " ".join(a)
        c.append(b)

    return c
