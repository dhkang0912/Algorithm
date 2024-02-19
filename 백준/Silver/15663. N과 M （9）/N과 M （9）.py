def dfs():
    pre = 0
    if len(ST) == M:
        print(*ST)
        return

    for i in range(len(lst)):
        if pre != lst[i] and not visited[i]:    # 방문하지 않은 칸, 그리고 lst[i]가 이전 값과 같지 않을 때
            ST.append(lst[i])
            pre = lst[i]
            visited[i] = True
            dfs()
            visited[i] = False
            ST.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

ST = []
visited = [0]*(N+1)
dfs()