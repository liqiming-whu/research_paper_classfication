# paper classification

依据摘要对文献进行分类(支持向量机）

tfidf: (9000, 47061)

Accuracy: 0.968
<<<<<<< HEAD

## usage：

```shell
python prediction.py --pmid 31519313  # 示例
```

```shell
python prediction.py --text 31519313.txt  # 示例文件
```

从pubmed id得到摘要，预测类别，或者从摘要文本预测类别

## requirements

```shell
pip install -r requirements.txt
```

```python
pandas
biopython
wget
scikit-learn
numpy
nltk  # 需要下载punkt数据：python >>>import nltk >>>nltk.download('punkt')
```

## data colletion

```python
get_data.py  # 获取各类文本存储在4个类别文件夹中。
make_other_data.py  # 获取"other"类数据。
merge_data.py  # 将数据整合为训练集和测试集。训练集：测试集=1800：300
```

## train

```shell
python svm.py  # 训练model，词汇表保存在word_dict.pikle，训练完毕后的模型保存在train_model.m。同时输出tfidf和accuracy
```

## test

```shell
python test_predict.py  #预测并输出测试集中100个样本的类别。
```

=======
>>>>>>> c99e7cccde247b84f401a49c82747b8ce0c19659
