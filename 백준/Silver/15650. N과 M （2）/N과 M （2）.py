def perm(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        if not visited[i]:
            path[level] = i
            visited[i] = 1
            perm(level+1, i+1)
            visited[i]=0




N, M = map(int, input().split())
path = [-1]*M
visited = [0]*(N+1)
visited[0] = 1
perm(0, 0)
