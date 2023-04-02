n = int(input())
for _ in range(n):
    c, s = input().split()
    c = int(c)
    for i in s:
        print(i * c, end='')
    print()