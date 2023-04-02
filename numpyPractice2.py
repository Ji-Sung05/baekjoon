import numpy as np
#np.random.random((2, 2))
print("임의 생성된 배열 값")
array = np.random.randint(0,100,(3,3))
print(array)
print("최대 값 : ", end = "")
print(np.max(array))