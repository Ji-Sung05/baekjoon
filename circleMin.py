def recursive(size, arr):
    print(min(arr))
    return ''

import numpy as np
arr = []
for i in range(5):
    a = np.random.randint(0,100)
    arr.append(a)
print(arr)
print("최소값: ", end = "")
result = recursive(4, arr)
print(result)