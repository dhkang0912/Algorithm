from collections import deque

def dfs(n):
    ST = []
    ST.append(n)
    answer = []

    while ST:
        v = ST.pop()

        if not visited_d[v]:
            visited_d[v] = True
            answer.append(v)

            for w in arr[v]:
                if not visited_d[w]:
                    ST.append(w)
    print(*answer)


def bfs(b_n):
    ST = []
    d_ST = deque(ST)
    d_ST.append(b_n)
    answer = []
    while d_ST:
        b_v = d_ST.popleft()

        if not visited_b[b_v]:
            visited_b[b_v] = True
            answer.append(b_v)

            for w in sorted(arr[b_v],reverse=False):
                if not visited_b[w]:
                    d_ST.append(w)

    print(*answer)



N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited_d = [False]*(N+1)
visited_b =[False]*(N+1)                    # bfs 방문

for i in range(M):                      # 인접행렬 만들기
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
for i in arr:
    i.sort(reverse=True)
dfs(V)
bfs(V)