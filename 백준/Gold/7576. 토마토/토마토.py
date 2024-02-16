from collections import deque

def sub(visited):
    for gr in range(N):
        for gc in range(M):
            if visited[gr][gc] == 0 and arr[gr][gc] == 0:
                return -1
    else:
        return max(map(max,visited))-1

def bfs():
    Q = deque()
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                Q.append((i,j))
                visited[i][j] = 1
    while Q:
        vr, vc = Q.popleft()

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newR = vr+dr
            newC = vc+dc
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC] and arr[newR][newC] != -1:
                Q.append((newR,newC))
                visited[newR][newC] = visited[vr][vc] + 1
    return sub(visited)


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sR = 0
sC = 0

print(bfs())