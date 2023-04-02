import math
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    min = math.lcm(a, b)
    print(min)
