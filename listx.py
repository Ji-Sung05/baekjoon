a, b = map(int, input().split())
list = list(map(int, input().split()))
for i in list:
    if b > i:
        print(i, end=" ")
