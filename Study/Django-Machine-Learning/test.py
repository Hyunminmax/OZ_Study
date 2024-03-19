## 타이타닉 생존자 예측 모델
# 탑승객 정보를 기반으로 >> 해당 탑승객의 생존 여부를 예측

# 데이터 로드
import pandas as pd

df_train = pd.read_csv("train.csv")
# df_train = pd.read_csv(".data/titanic/train.csv")
print(df_train.head(3))

# df_test = pd.read_csv(".data/titanic/test.csv")
# df_test

# # EDA (Exploratory Data Analysis) -> 데이터 탐험 (데이터의 유무 확인)
# print(df_train.columns) # train
# print(df_test.columns) # test

# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')
# Index(['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch',
#        'Ticket', 'Fare', 'Cabin', 'Embarked'],
#       dtype='object')

# print(df_train)

# print(df_train.shape)
# print(df_test.shape)

# (891, 12)
# (418, 11)

# print(df_train.info())
# print(df_test.info())