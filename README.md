# 딥러닝

## 퍼셉트론

퍼셉트론(인공뉴런)은 다수의 신호를 받아 하나의 신호를 출력한다.

신호의 흐름은 0과 1의 값을 가진다(boolean).



## 다층 퍼셉트론

단층 퍼셉트론으로는 XOR게이트를 표현할 수 없다. == 단층 퍼셉트론으로 비선형 영역을 분리할 수 없다.

기존 게이트(AND, OR, NAND)를 조합하여 층을 쌓으면 XOR게이트를 구현할 수 있다.



XOR게이트 진리표

| x1   | x2   | s1   | s2   | y    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | 0    | 1    | 0    | 0    |
| 0    | 1    | 1    | 1    | 1    |
| 1    | 0    | 1    | 1    | 1    |
| 1    | 1    | 0    | 1    | 0    |



## 인공신경망

### 구성

입력층, 은닉층, 출력층

활성화 함수를 이용한 퍼셉트론 식

y=h(b+w1\*x1 + w2\* x2)

h(x) = 0 (x<=0)

​		= 1(x>0)

입력신호의 총합을 출력신호로 변환하는 함수를 "활성화 함수"라고 한다.

### 시그모이드(sigmoid) 함수

신경망에서 자주 이용하는 활성화 함수 중의 하나

**표현식**

h(x) = 1/(1+exp(-x))

