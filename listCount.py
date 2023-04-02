n = int(input())
list = list(map(int, input().split()))
a = int(input())
if a in list:
    print(list.count(a))