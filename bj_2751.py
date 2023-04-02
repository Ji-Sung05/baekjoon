import sys
n = int(sys.stdin.readline())
q = [0] * 10001
for i in range(n):
    data = int(sys.stdin.readline())
    q[data] += 1

for i in range(10001):
    if q[i] != 0:
        for j in range(q[i]):
            print(i)