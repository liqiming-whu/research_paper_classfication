biology = "d:/research_paper_classfication/biology/"
chemistry = "d:/research_paper_classfication/chemistry/"
physics = "d:/research_paper_classfication/physics/"
computer_science = "d:/research_paper_classfication/computer_science/"
other = "d:/research_paper_classfication/other/"


# 合并各类数据
# 执行merge_data前务必删除train_data.csv和test_data.csv。
def merge_data(name):
    f1 = open(biology+name).read()
    f2 = open(chemistry+name).read()
    f3 = open(physics+name).read()
    f4 = open(computer_science+name).read()
    f5 = open(other+name, encoding="utf-8").read()
    with open(name, "a", encoding="utf-8") as f:
        f.write(f1)
        f.write(f2)
        f.write(f3)
        f.write(f4)
        f.write(f5)


merge_data("train_data.csv")
merge_data("test_data.csv")
