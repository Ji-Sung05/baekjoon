from sys import stdin

array = [True for i in range(1000001)]

for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(stdin.readline())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break

# 에라토스테네스의 체
# array = [True for i in range(1000001)]

#   for i in range(2, 1001):
#       if array[i]:
#           for k in range(i + i, 1000001, i):
#               array[k] = False

# (1) 전체 수 만큼 True의 리스트를 생성해준다.
# (2) 2부터 +1씩 해주면서 그 배수에 해당하는 값들을 False로 바꿔준다.

# 그러면 array에는 소수에 해당하는 값만 True 값을 가지고 있기 때문에
# 이후로는 True값을 가졌을 때 원하는 계산을 해주면 된다.
# 소수 리스트를 구했다면 이제는

# 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.

# 이 조건을 만족하도록 출력해야 한다.

# 나는 array의 길이만큼 for문을 돌리되, i가 작은 수부터 시작되기 때문에
# 만약 array[i]와 array[n-i]가 둘다 array에 존재할 경우 해당 값을 출력하고 바로 break를 걸었다.
# https://velog.io/@dding_ji/%EB%B0%B1%EC%A4%80-6588.-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-Python-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
