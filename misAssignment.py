list = []
for i in range(1, 29):
    a = int(input())
    list.append(a)
for i in range(1, 31):
    if i not in list:
        print(i)
#removed를 사용할 수도 있다.