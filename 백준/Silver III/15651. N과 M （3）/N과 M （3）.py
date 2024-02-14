def dfs():
    if len(ST) == M:
        print(*ST)
        return

    for i in range(1, N+1):
        ST.append(i)
        dfs()
        ST.pop()


N, M = map(int, input().split())
ST = []

dfs()