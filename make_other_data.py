import pandas as pd
import csv
import wget
import tarfile

# 下载维基百科词条，截取部分作为other类
dbpedia_url = 'https://github.com/le-scientifique/torchDatasets/raw/master/dbpedia_csv.tar.gz'
wget(dbpedia_url)
with tarfile.open("dbpedia_csv.tar.gz", "r:gz") as tar:
    tar.extractall()

df = pd.read_csv("dbpedia_csv/test.csv", names=["class", "title", "content"])
df2 = df.sample(frac=0.03)
title = df2["title"]
content = df2["content"]

with open("d:/research_paper_classfication/other/train_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for t, c in zip(title[:1800], content[:1800]):
        writer.writerow([t, c, "5"])


with open("d:/research_paper_classfication/other/test_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for t, c in zip(title[1800:], content[1800:]):
        writer.writerow([t, c, "5"])
