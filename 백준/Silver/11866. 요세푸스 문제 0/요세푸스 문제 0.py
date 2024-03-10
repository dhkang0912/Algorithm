import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K -= 1
lst = [i for i in range(1, N+1)]
# print(lst)

stack = []
stack.append(lst.pop(K))
idx = K

while len(stack) < N:
    idx += K
    if idx > len(lst) - 1:
        while True:
            idx -= len(lst)
            if idx <= len(lst)-1:
                break
    stack.append(lst.pop(idx))
print('<', end='')
for i in range(len(stack)):
    if i < len(stack)-1:
        print(stack[i], end =', ')
    else:
        print(stack[i], end='')
print('>')