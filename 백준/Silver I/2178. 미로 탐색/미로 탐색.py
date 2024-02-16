from collections import deque
def bfs(r,c):
    Q = deque()
    visited = [[0]*M for _ in range(N)]
    Q.append((r,c))

    while Q:
        vr, vc = Q.popleft()
        visited[r][c] = 1

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newR = vr+dr
            newC = vc+dc

            if 0<=newR<N and 0<=newC<M and not visited[newR][newC] and arr[newR][newC]=='1':
                Q.append((newR,newC))
                visited[newR][newC] = visited[vr][vc] + 1
    print(visited[N-1][M-1])



N, M = map(int, input().split())
arr = [input() for _ in range(N)]
bfs(0,0)