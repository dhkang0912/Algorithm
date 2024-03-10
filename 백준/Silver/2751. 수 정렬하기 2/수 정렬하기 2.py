import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    i = int(input())
    lst.append(i)
lst.sort()
# print(lst)

for j in lst:
    print(j)