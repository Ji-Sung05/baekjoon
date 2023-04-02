def recursive(n, r):
    if r == 0:
        return 1
    else:
        return n * recursive(n - 1, r - 1)
print("숫자를 입력하세요: ")
n, r = map(int, input().split())
result = recursive(n, r)
print(result)