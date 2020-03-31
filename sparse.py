import numpy as np
from scipy import sparse

b1 = np.eye(4, dtype=int)
print("Numpy 배열: \n{}".format(b1))

# sparse.csr_matrix() 메소드: 0이 아닌 원소만 저장
sparse_matrix = sparse.csr_matrix(b1)
print("scipy의 CSR 행렬: \n{}".format(sparse_matrix))

b2 = np.eye(5, k=-1, dtype=int)
print(b2)

sparse_matrix = sparse.csr_matrix(b2)
print("scipy의 CSR 행렬: \n{}".format(sparse_matrix))
b3 = np.arange(16).reshape(4,4)
print(b3)

x = np.diag(b3)
print(x)
y = np.diag(np.diag(b3))
print('------------')
print(y)

# COO 포맷 (coordinate)
data = np.ones(4)
print(data)

row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data,(row_indices,col_indices)))
print("COO")
print(eye_coo)
