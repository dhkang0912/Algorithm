from collections import deque

def bfs(row, col):
    Q = deque()
    Q.append((row, col))
    arr[row][col] = 0

    while Q:
        row, col = Q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            new_row = row + dr
            new_col = col + dc
            if 0 <= new_row <= h-1 and 0 <= new_col <= w-1 and arr[new_row][new_col]==1:
                Q.append((new_row,new_col))
                arr[new_row][new_col] = 0

while True:
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    # print(arr)
    cnt = 0
    if w == 0 and h == 0 :
        break
    else:
        for row in range(h):
            for col in range(w):
                if arr[row][col] == 1:
                    cnt += 1
                    bfs(row, col)

    print(cnt)