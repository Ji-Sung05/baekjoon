a, b = map(int, input().split())

stack1 = []
stack2 = []

for i in range(a):
    if a % (i+1) == 0:
        stack1.append(i + 1)
for i in range(b):
    if b % (i+1) == 0:
        stack2.append(i + 1)
intersection = list(set(stack1) & set(stack2))
n1 = max(intersection)
n2 = a / n1
n3 = b / n1
print(n1)
print(int(n1 * n2 * n3))
