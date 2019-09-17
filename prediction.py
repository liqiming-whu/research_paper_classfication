import argparse
from data_utils import*
import get_data
from test_predict import*


def load_data(args):  
    if args.pmid:
        abstract_list = get_abstract_id(args.pmid)
        return abstract_list
    elif args.text:
        abstract_list = get_abstract_text(args.text)
        return abstract_list
    else:
        return False


def get_abstract_id(pmid):
    _, abstract_list = get_data.get_abstract("pubmed", [pmid])

    return abstract_list


def get_abstract_text(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    abstract_list = [text]

    return abstract_list


def build_data(x, word_dict):
    x = list(map(lambda d: word_tokenize(clean_str(d)), x))
    x = list(map(lambda d: list(
        map(lambda w: word_dict.get(w, word_dict["<unk>"]), d)), x))
    x = list(map(lambda d: d + [word_dict["<eos>"]], x))

    return x


def main(args):
    word_dict = build_word_dict()
    abstract_list = load_data(args)
    if(abstract_list):
        text = build_data(abstract_list, word_dict)
        clf = load_model()
        if(clf):
            text = addwhitespace(text)
            predicted = predict(text, clf)
            predict_dict = build_predict_dict()
            predict_class = list(predict_dict[i] for i in predicted)
            print("class:", " ".join(predict_class))
    else:
        print("""An error has occurred, probably because:
1.No parameters. Please input Pubmed id or txt file.
2.Sometimes PubMed hasn't got the full abstract yet.
Change another or read the original paper.""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Input:pubmed id. Output:class.",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--pmid", dest="pmid", type=str, default=False,
                        help="Pubmed id.")
    parser.add_argument("--text", dest="text", type=str, default=False,
                        help="abstract.txt file")
    args = parser.parse_args()

    main(args)
