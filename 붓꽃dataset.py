from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
irisData = load_iris()
# print(irisData)
# load_iris()함수가 리턴하는 객체: Bunch 클래스 객체
# Bunch 클래스 객체는 파이썬의 딕셔너리와 유사하게 key와 value로 구성되어 있다.

# 훈련데이터와 테스트데이터를 나누기 위한 함수
#  train_test_split 모듈에 있는 train_test_split()
#  train_test_split모듈 import:  skelarn.model_selection

# scikit-learn에서 데이터는 대문자 X로 표시하고 레이블은 소문자 y로 표시한다.

X_tarin, X_test, y_train, y_test = train_test_split(irisData['data'], irisData['target'], random_state=0)
print(X_tarin.shape)
print(X_test.shape)