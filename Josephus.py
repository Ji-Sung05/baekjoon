from collections import deque
a, b = map(int, input().split())
q = deque()
for i in range(1, a + 1):
    q.append(i)
print("<", end = '')
while q:
    for i in range(b - 1):   
       q.append(q.popleft())
    print(q.popleft(), end = ', ')
    if len(q) == 1:
        print(q.popleft(), end = '>')