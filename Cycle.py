n = input()
num = n
cnt = 0

while 1:
    a = int(num) // 10
    b = int(num) % 10
    plus = str(int(a) + int(b))
    c = num[-1] + plus[-1]
    num = c
    cnt += 1
    if num == n:
        print(cnt)
        break