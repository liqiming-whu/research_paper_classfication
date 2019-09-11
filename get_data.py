from Bio import Entrez
from Bio import Medline
import csv


Entrez.email = "liqiming1914658215@gmail.com"
Entrez.api_key = "c80ce212c7179f0bbfbd88495a91dd356708"
# path = "d:/research_paper_classfication/biology/"
path = "d:/research_paper_classfication/chemistry/"
db = "pubmed"
# keywds = "Cell[ta]"
keywds = "Nat Chem[ta]"
# sub = "biology"
sub = "chemistry"


def search(database, keywords):
    handle = Entrez.esearch(db=database, term=keywords, retmax=2400)
    record = Entrez.read(handle)

    return record["Count"], record["IdList"]


def get_abstract(database, idlist):
    handle = Entrez.efetch(db=database, id=idlist, rettype="medline",
                           retmode="text")
    records = Medline.parse(handle)
    records = list(records)

    title_list = []
    abstract_list = []
    for record in records:
        title = record.get("TI", "?")
        abstract = record.get("AB", "?")
        if not abstract == "?":
            title_list.append(title)
            abstract_list.append(abstract)

    return title_list, abstract_list


def make_train_data(title_list, abstract_list, tag):
    with open(path+"train_data.csv", "w",
              newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        print("make train data...")
        for title, abstract in zip(title_list[:1200], abstract_list[:1200]):
            writer.writerow([title, abstract, tag])


def make_test_data(title_list, abstract_list, tag):
    with open(path+"test_data.csv", "w",
              newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        print("make test data...")
        for title, abstract in zip(title_list[1200:], abstract_list[1200:]):
            writer.writerow([title, abstract, tag])


def main(database, keywords, tag):
    count, idlist = search(database, keywords)
    print("count:"+count)
    title_list, abstract_list = get_abstract(database, idlist)
    print("list length:"+str(len(title_list)))
    make_train_data(title_list, abstract_list, tag)
    make_test_data(title_list, abstract_list, tag)
    print("done!")


if __name__ == "__main__":
    main(db, keywds, sub)
