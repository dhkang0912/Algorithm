from collections import deque
import sys
input = sys.stdin.readline

Q = deque()
T = int(input())
for tc in range(T):
    order = input().strip()
    if 'push' in order:
        order, n = order.split()
        n = int(n)
        if 'back' in order:
            Q.append(n)
        elif 'front' in order:
            Q.appendleft(n)
            # Q[0], Q[-1] = Q[-1], Q[0]
    elif order == 'pop_front':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if Q:
            print(Q.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(Q))
    elif order == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif order == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)

