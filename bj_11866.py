import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
q = deque()

for i in range(a):
    q.append(i + 1)
print("<", end = "")
while(len(q) != 1):
    for i in range(b - 1):
        q.append(q.popleft())
    print(str(q.popleft()) + ",", end = " ")
print(q.popleft(), end = "")
print(">")