import sys
input = sys.stdin.readline


N = int(input())

num = 1
stack = []
while num <= N:
    order = input().strip()
    # print(order)
    if 'push' in order:
        order, n = order.split()
        n = int(n)
        # print(order)
        # print(n)
    if order == 'push':
        stack.append(n)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    num += 1