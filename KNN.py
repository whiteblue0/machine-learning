# K Nearest Neighbors(최근접 이웃 알고리즘)
# 훈련데이터에서 새오로운 데이터에 가장 가까운 k개의 이웃을 찾는다
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

irisData = load_iris()
X_tarin, X_test, y_train, y_test = train_test_split(irisData['data'], irisData['target'], random_state=0)
# KNeighborsClassifier 매개변수 : n_neighbors
knn = KNeighborsClassifier(n_neighbors=1)
print(knn.fit(X_tarin,y_train))

X_newData = np.array([[5.1, 2.9, 1, 0.3]])

print(X_newData.shape)
prediction = knn.predict(X_newData)
print(prediction)
print(irisData['target_names'][prediction])
y_predict = knn.predict(X_test)
acc = np.mean(y_predict==y_test)
print("accuracy:",acc)
print(knn.score(X_test,y_test))