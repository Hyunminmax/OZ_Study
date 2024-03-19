import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas   as pd

iris = load_iris() #feature data
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=99)
print('x_train', x_train)
print('x_test', x_test)
print('y_train', y_train)
print('y_test', y_test)