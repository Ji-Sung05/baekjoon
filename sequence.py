n = int(input())
stack = []
answer = []
a = 1
flag = 0
for i in range(n):
    num = int(input())
    while a <= num:
        stack.append(a)
        answer.append('+')
        a += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)