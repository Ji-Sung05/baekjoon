n = int(input())
q = []
for i in range(n):
    q.append(int(input()))
q.sort()
for i in range(n):
    print(q[i])