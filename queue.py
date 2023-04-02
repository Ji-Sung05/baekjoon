import sys
from collections import deque

n = int(input())
q = deque([])
for i in range(n):
    number = sys.stdin.readline().split()
    if number[0] == 'push':
        q.append(number[1])
    elif number[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif number[0] == 'size':
        print(len(q))
    elif number[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif number[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif number[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)