import numpy as np
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

from data_utils import *


class Svm(object):
    def __init__(self):
        self.word_dict = build_word_dict()
        self.vocabulary_size = len(self.word_dict)
        self.train_x, self.train_y = build_svm_dataset("train", self.word_dict)
        self.test_x, self.test_y = build_svm_dataset("test", self.word_dict)

    def make_tfidf(self, train_x):  # 特征提取：tf-idf词频矩阵
        vectorizer = CountVectorizer()
        tfidftransformer = TfidfTransformer()
        tfidf = tfidftransformer.fit_transform(
            vectorizer.fit_transform(train_x))

        return tfidf

    def train(self, train_x):  # 利用scikit的管道和svm模型进行训练
        text_clf = Pipeline([("vect", CountVectorizer()),
                             ("tfidf", TfidfTransformer()),
                             ("clf", SVC(C=1, kernel="linear"))])
        text_clf = text_clf.fit(train_x, self.train_y)
        print("train finished.")

        return text_clf

    def predict(self, text_clf, test_x):   # 预测获取准确率
        predicted = text_clf.predict(test_x)
        accuracy = np.mean(predicted == self.test_y)

        return accuracy

    def save_model(self, text_clf):  # 保存model
        joblib.dump(text_clf, "train_model.m")

    def main(self):
        train_x = addwhitespace(self.train_x)
        test_x = addwhitespace(self.test_x)
        tfidf = self.make_tfidf(train_x)
        print("tfidf:", tfidf.shape)
        text_clf = self.train(train_x)
        self.save_model(text_clf)
        acc = self.predict(text_clf, test_x)

        print("Accuracy:", acc)


if __name__ == "__main__":
    Svm().main()
