# encoding=utf-8
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn import svm
from sklearn import metrics
import re
import time

def ReadCSV(Path):
    dates = []
    tems = []
    weas = []
    winds = []
    strengths = []
    laebls = []
    data = pd.read_csv(Path, names=['date', 'tem', 'wea', 'wind', 'strength'], encoding='GB2312')
    for i in range(len(data)):
        line=data.iloc[i,:]
        date = re.findall(r'\d+', line['date'])
        dates.append(date)

        tem = re.findall(r'\d+', line['tem'])
        tems.append(tem)

        strength = re.findall(r'\d-\d|<\d', line['strength'])
        strengths.append(strength[0])

        wind = line['wind'].encode(encoding='utf-8')
        winds.append(wind)

        wea = line['wea'].encode(encoding='utf-8')
        weas.append(wea)

        laebl = line['laebl'].encode(encoding='utf-8')
        laebls.append(laebl)

    return [dates, tems, weas, winds, strengths, labels]

def Preprocess(Path):
    features = []
    labels = []
    sample = ReadCSV(Path)
    for i in range(len(sample[0])):
        features.append([sample[1][i], sample[2][i], sample[3][i], sample[4][i]])
        labels.append(sample[-1][i])

    train_features, test_features, train_labels, test_labels = \
        train_test_split(features, features, test_size=0.33, random_state=0)
    return train_features, test_features, train_labels, test_labels

def predictTree(Path):
    train_features, test_features, train_labels, test_labels = Preprocess(Path)
    clf = DecisionTreeClassifier(criterion='gini')
    start = time.time()
    clf = clf.fit(train_features, train_labels)
    test_predict = clf.predict(test_features)
    score = accuracy_score(test_labels, test_predict)
    end = time.time() - start
    print("CART 分类树准确率 %.4lf" % score, 'time is ', end)

def predictSVC(Path):
    train_features, test_features, train_labels, test_labels = Preprocess(Path)
    model = svm.SVC()
    start = time.time()
    model.fit(train_features,train_labels )
    prediction=model.predict(test_features)
    end = time.time() - start
    print('SVM 分类准确率: ', metrics.accuracy_score(prediction, test_labels), 'time is ', end)

def main():
    Path = 'E:/weather/weather/weather/data/weather.csv'
    predictTree(Path)
    predictSVC(Path)

if __name__ == '__main__':
    main()
