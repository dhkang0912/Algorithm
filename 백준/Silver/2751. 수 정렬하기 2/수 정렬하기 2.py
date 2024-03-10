import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*N
for i in range(N):
    j = int(input())
    lst[i]=j
lst.sort()
# print(lst)

for z in lst:
    print(z)