list = []
for i in range(5):
    list.append(int(input()))
avg = sum(list) / len(list)
list.sort()
n = int(len(list) / 2)
mid = list[n]
print(int(avg))
print(mid)