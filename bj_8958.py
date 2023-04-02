import sys
n = int(sys.stdin.readline())

for _ in range(n):
    ox = sys.stdin.readline()
    o = 0
    sum = 0
    for i in ox:
        if(i == 'O'):
            o+=1
            sum += o
        elif(i == 'X'):
            o = 0      
    print(sum) 