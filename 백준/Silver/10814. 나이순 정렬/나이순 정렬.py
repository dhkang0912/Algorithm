import sys
input = sys.stdin.readline
N = int(input())
lst = []
# lst = [list(input().split()) for _ in range(N)]
for _ in range(N):
    age, name = input().split()
    age = int(age)
    lst.append([age, name])

lst.sort(key= lambda x:x[0])

for j in lst:
    print(*j)

