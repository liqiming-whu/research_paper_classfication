from sklearn.externals import joblib
from svm import Svm
from data_utils import*


def load_model():
    try:
        return joblib.load("train_model.m")
    except IOError:
        print("no model loaded.")
        return False


def predict(text, clf):
    predicted = clf.predict(text)

    return predicted


def main():
    word_dict = build_word_dict()
    test_x, _ = build_svm_dataset("test", word_dict)
    clf = load_model()
    if(clf):
        text = addwhitespace(test_x)
        predicted = predict(text, clf)
        print("class", predicted)


if __name__ == "__main__":
    main()
