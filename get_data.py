from Bio import Entrez
from Bio import Medline
import csv


Entrez.email = "liqiming1914658215@gmail.com"
Entrez.api_key = "c80ce212c7179f0bbfbd88495a91dd356708"
path = "d:/research_paper_classfication/biology"


def search(database, keywords):
    handle = Entrez.esearch(db=database, term=keywords, retmax=2000)
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
        title_list.append(record.get("TI", "?"))
        abstract_list.append(record.get("AB", "?"))

    return title_list, abstract_list


def make_train_data(title_list, abstract_list, tag):
    with open("train_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for title, abstract in title_list[:1800], abstract_list[:1800]:
            writer.writerow([title_list, abstract_list, tag])


def make_test_data(title_list, abstract_list, tag):
    with open("test_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for title, abstract in title_list[1800:], abstract_list[1800:]:
            writer.writerow([title_list, abstract_list, tag])


def main(database, keywords, tag):
    count, idlist = search(database, keywords)
    print(count)
    title_list, abstract_list = get_abstract(database, idlist)
    make_train_data(title_list, abstract_list, tag)
    make_test_data(title_list, abstract_list, tag)


if __name__ == "__main__":
    main("pubmed", "Cell[ta]", "biology")
