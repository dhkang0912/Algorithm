def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        path[level] = i
        perm(level+1)



N, M = map(int, input().split()) # N까지 숫자, M개를 고름
path = [-1] * M
perm(0)