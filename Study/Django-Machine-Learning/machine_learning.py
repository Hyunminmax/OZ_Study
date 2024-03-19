import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas   as pd

iris = load_iris() #feature data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=99)
# print('X_train', X_train)
# print('X_test', X_test)
# print('y_train', y_train)
# print('y_test', y_test)
# print(y_test)
# 2. 학습을 위한 알고리즘을 불러온다. 
from sklearn.tree  import DecisionTreeClassifier #분류 알고리즘
dt_clf = DecisionTreeClassifier(random_state=123)
# print(dt_clf)
#3. 학습을 진행합니다. >> train_data(X_train, y_train)//모의고사
dt_clf.fit(X_train, y_train)    #fit() - 학습을 진행

# 4. 시험을 치러 갑니다. >> test_data(X_test, y_test) // 수능시험
# predict() >> 예측해봐
predict = dt_clf.predict(X_test)
# print(predict)

# 5. 채점을 진행합니다. 
# accuracy_score()

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predict))
df = pd.DataFrame(data=X_test, columns=iris.feature_names)
df['answer'] = y_test
df['predict'] = predict

# print(df)

iris = load_iris()
dt_clf = DecisionTreeClassifier()
dt_clf.fit(iris.data, iris.target)
pred = dt_clf.predict(iris.data)
print(accuracy_score(iris.target, pred))