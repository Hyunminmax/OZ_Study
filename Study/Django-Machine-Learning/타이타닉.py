# -*- coding: utf-8 -*-
"""타이타닉.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKm6oJoJ4t364qCVsfNxZPvzvyc7r1SI
"""

# 데이터 로드
import pandas as pd

df_train = pd.read_csv("train.csv")
df_train.head(3)

df_test = pd.read_csv("test.csv")
df_test

# EDA (Exploratory Data Analysis) -> 데이터 탐험 (데이터의 유무 확인)
print(df_train.columns) # train
print(df_test.columns) # test

print(df_train.shape)
print(df_test.shape)

(891, 12)
(418, 11)

print(df_train.info())
print(df_test.info())

# null 갯수 체크
print(df_train.isna().sum())
print(df_test.isna().sum())

# 어떤 컬럼을 살리고, 어떤 컬럼을 지울 것인가? => 시각화를 통해 진행
import matplotlib.pyplot as plt
import seaborn as sns

def bar_chart(column_name):
    # df_train[df_train["Survived"] == 1]
    # df_train[df_train["Survived"] == 1]["Pclass"] # Pclass 컬럼의 데이터 출력

    survived = df_train[df_train["Survived"] == 1][column_name].value_counts()
    dead = df_train[df_train["Survived"] == 0][column_name].value_counts()

    df_merged = pd.DataFrame({"Survived":survived, "Dead": dead})
    df_merged.plot(kind="bar", stacked=True, figsize=(12,8))

bar_chart("Embarked")

# 가장 많은 요금을 낸 상위 10명의 생존율은 어떻게 될까요?
# df_train.sort_values(by="Fare", ascending=False).head(10)[["Survived", "Fare"]] # Fare : 요금에 따라서 정렬
# head(5) 상위 5명 || tail(5) 하위 5명
# df_train.sort_values(by="Fare", ascending=False).head(10)[["Survived", "Fare"]].value_counts() # 인원 카운트
df_train.sort_values(by="Fare", ascending=False).head(10)[["Survived"]].value_counts() # 인원 카운트

df_train[["Name","Survived"]]

# 이름으로 값들 추려서 확인
train_test_data = [df_train, df_test]

for data in train_test_data:
  data["Name"] = data["Name"].str.extract(" ([A-Za-z]+)\. ") # extract 추출하기

df_train["Name"]
# df_train["Name"].value_counts()

# 문자열 -> 숫자형 데이터로 변경
name_mapping = {
    "Mr": 0, "Miss": 1, "Mrs": 2, "Master": 3, "Dr": 4, "Rev": 5
}

for data in train_test_data:
  data["Name"] = data["Name"].map(name_mapping)

df_train["Name"].value_counts()

bar_chart("Name")

# Sex
df_train["Sex"] = df_train["Sex"].replace({"male":0, "female":1})
df_test["Sex"] = df_test["Sex"].replace({"male":0, "female":1})

df_train["Sex"].value_counts()
df_test["Sex"].value_counts()
df_train

# Age
df_train["Age"].isna().sum()

df_train.groupby("Name")["Age"].mean()

df_train["Age"].fillna(df_train.groupby("Name")["Age"].transform("mean"), inplace=True)
df_test["Age"].fillna(df_test.groupby("Name")["Age"].transform("mean"), inplace=True)

df_train["Age"].isna().sum()

df_test["Age"].isna().sum()

df_test["Age"].fillna(df_test["Age"].mean(), inplace=True) # Nan인 부분을 변경
df_test["Age"].isna().sum() # null 데이터 갯수 확인

# Age

df_train["Age"].value_counts()

df_train["Age"].isna().sum() # null 데이터 갯수 확인

import numpy as np

# age_bins = [0, 16, 32, np.inf] #inf: infinite
age_bins = [0, 16, 32, 55, 100]
age_labels = [0, 1, 2, 3]

for data in train_test_data:
  data["Age"] = pd.cut(data["Age"], bins=age_bins, labels=age_labels)

df_train["Age"].value_counts()

# SibSp, Parch
# df_train["Family"] = df_train["SibSp"] + df_train["Parch"] + 1
# df_test["Family"] = df_train["SibSp"] + df_train["Parch"] + 1

# 위 아래 둘 중 하나 사용 하기

for data in train_test_data:
  data["Family"] = data["SibSp"] + data["Parch"] + 1

df_train["Family"].value_counts()

# Fare
df_train["Fare"].isna().sum() # null 데이터 갯수 체크

fare_bins = [0, 20, 100, 1000]
fare_labels = [0, 1, 2]

for data in train_test_data:
  data["Fare"] = pd.cut(data["Fare"], bins=fare_bins, labels=fare_labels)

df_train["Fare"].value_counts()

# Embarked
df_train["Embarked"] = df_train["Embarked"].replace({"S":0, "C":1, "Q":2})
df_test["Embarked"] = df_train["Embarked"].replace({"S":0, "C":1, "Q":2})

df_test["Age"].fillna(0, inplace=True)
df_test["Age"].isna().sum()

df_train["Embarked"].value_counts()

df_train["Embarked"].fillna(0, inplace=True)
df_test["Embarked"].fillna(0, inplace=True)

df_train["Embarked"].isna().sum()
df_test["Embarked"].isna().sum()

# drop_train_cols = ["Embarked", "SibSp", "Parch", "Ticket", "Cabin"]
drop_train_cols = ["PassengerId", "SibSp", "Parch", "Ticket", "Cabin"]

df_train_final = df_train.drop(drop_train_cols, axis=1)
df_train_final

df_test # 데이터 목록 확인용 (생략가능)

drop_test_cols = ["SibSp", "Parch", "Ticket", "Cabin"]

df_test_final = df_test.drop(drop_test_cols, axis=1)
df_test_final

"""# 모델링"""

df_train_final.fillna(0, inplace=True)
df_train_final.isna().sum()

df_test_final.fillna(0, inplace=True)
df_test_final.isna().sum()

features = df_train_final.drop("Survived", axis=1)
labels = df_train_final["Survived"]

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

# kfold
kfold = KFold(n_splits=10, shuffle=True, random_state=123)
dt_clf = DecisionTreeClassifier()
scores = cross_val_score(dt_clf, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# RandomForestClassifier
rf = RandomForestClassifier(n_estimators=5)
scores = cross_val_score(rf, features, labels, cv=kfold, scoring="accuracy")

# scores
print(np.mean(scores)*100)

# GaussianNB
gb = GaussianNB()
scores = cross_val_score(gb, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

# SVC
svc = SVC()
scores = cross_val_score(svc, features, labels, cv=kfold, scoring="accuracy")

print(np.mean(scores)*100)

df_train_final

df_test_final

# SVC 알고리즘을 사용해서 최종 결과 값 도출
svc = SVC()
svc.fit(features, labels)

# 수능 문제는?
test_data = df_test_final.drop("PassengerId", axis=1)
test_data

pred = svc.predict(test_data)
pred

df_final_submit = pd.DataFrame({
    "PassengerId": df_test_final["PassengerId"],
    "Survived": pred
    })
df_final_submit.set_index("PassengerId", inplace=True)

df_final_submit.to_csv("submission.csv")