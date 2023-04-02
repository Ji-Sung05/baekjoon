def recursive(x):
    if x == 1:
        return x
    else:
        return x + recursive(x - 1)


print("숫자를 입력하세요: ")
result = recursive(int(input()))
print(result)
