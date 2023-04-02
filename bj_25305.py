a, b = map(int, input().split())
l = []
l = list(map(int, input().split()))
l.sort(reverse = True)
print(l[b - 1])