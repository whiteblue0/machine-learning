import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,6,0.1)
y = np.sin(x)

# 그래프 그리기
plt.plot(x,y)
# plt.show()

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")

plt.legend()
plt.show()