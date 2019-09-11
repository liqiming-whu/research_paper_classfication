biology = "d:/research_paper_classfication/biology/"
chemistry = "d:/research_paper_classfication/chemistry/"


def merge_data(name):
    f1 = open(biology+name).read()
    f2 = open(chemistry+name).read()
    with open(name, "a", encoding="utf-8") as f:
        f.write(f1)
        f.write(f2)


merge_data("train_data.csv")
merge_data("test_data.csv")
