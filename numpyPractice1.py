import numpy as np

arr_test = np.array(
    [  # 1차 array
        [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]  # 2차 array
    ]
)
print(arr_test)

print(np.min(arr_test))
print(np.max(arr_test))