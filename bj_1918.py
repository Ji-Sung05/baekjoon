#아직 못 푼 문제
import sys
def prec(op):
    if op == '(' and ')':
        return 0
    elif op == '+' and '-':
        return 1
    elif op == '*' and '/':
        return 2
    else:
        return -1
    
stack = []
str = sys.stdin.readline()
for i in range(len(str)):
    ch = str[i]
    if ch == '+' and '-' and '*' and '/':
        while(prec(ch) <= prec(stack[0])):
            print(stack.pop(), end='')
        stack.append(ch)
        
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        top_op = stack.pop()
        while(top_op != '('):
            print(top_op, end='')
            top_op = stack.pop()
    else:
        print(ch, end='')
while(stack):
    print(stack.pop(), end='')