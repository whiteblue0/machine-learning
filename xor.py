from sklearn import svm

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

# 주어진 데이터 분리
data = []
label = []

for row in xor_data:
    p=row[0]
    q=row[1]
    res=row[2]

    data.append([p,q])
    label.append(res)

# svm 알고리즘을 사용하는 기계학습 객체를 만든다
clf = svm.SVC()

# fit() method: 객체에 데이터를 학습시킨다
print(clf.fit(data,label))

# predict() method: 학습데이터를 이용하여 예측한다
pre = clf.predict(data)
print(pre)

cnt = 0
total = 0

for idx,ans in enumerate(label):
    p = pre[idx]
    if p == ans:
        cnt += 1
        total += 1

print("정확도:", cnt ,'/', total, '=', cnt/total)