a, b = map(int, input().split())

if a == 0:
    if b >= 45:
        print(f"{a} {b - 45}")
    else:
        min = 60 - (45 - b)
        print(f"{23} {min}")
else:
    if b >= 45:
        print(f"{a} {b - 45}")
    else:
        min = 60 - (45 - b)
        print(f"{a - 1} {min}")