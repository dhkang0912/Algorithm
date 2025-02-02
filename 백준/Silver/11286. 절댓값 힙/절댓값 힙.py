import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())

heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        print(heappop(heap)[1] if heap else 0)
    else:
        heappush(heap, (abs(x), x))