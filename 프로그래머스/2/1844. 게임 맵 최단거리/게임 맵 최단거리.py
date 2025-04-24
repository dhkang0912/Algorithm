'''
최대한 쪼개서 생각해보자

상대 팀 진영을 먼저 파괴하기 => 이기는 조건
상대 팀 진영에 최대한 빨리 도착하기

맵 = 5*5 크기
내 캐릭터는 1,1 시작 => (0,0)이 아닌 (1,1)부터 시작

상대 진영은 (5,5) 위치에 있음 => (5,5)까지 최대한 빨리 도착해야함

검은색은 벽이라서 갈 수 없음
한번에 움직일 수 있는 방향은 상하좌우 1칸씩 => 4방향을 탐색하여 움직일 수 있음

만약 상대 진영에서 입구에 벽을 다 쳐놓은 경우 도달하지 못할 수도 있음

# input
maps => 0,1 (1 = 갈 수 있음) => 이차원 배열

# output
- 지나가야 하는 최솟값 return
- 만약 도달 못하면 -1 return

# 로직
최소 거리를 찾는 거라서 visited를 통해서 이전에 방문했던 거리 +1을 하면 되는 문제라고 생각됨
핵심은 좌측 상단에서 시작하여 우측 하단으로 향해야 하는 것 => 결국 도착하는 위치에 맞춰서 총 걸리는 거리 중 가장 적은 것을 반환

dfs 재귀로 문제를 푼다고 생각
1. visited 배열이 필요
2. 실제로 얼마나 비용이 들었는지를 추가할 리스트가 필요 => distance
2. 시작 지점과 종료 지점이 필요
=> 시작 지점 (0,0)
=> 종료 지점 maps의 크기를 알아야 함
len(maps[0]) => 열의 크기, c - 1
for문으로 행의 크기 알기 = > r - 1
3. dfs의 시작은 좌표 0,0
3-1. 만약 좌표가 종료 지점에 도착하면 visited에서 가장 큰 걸 distance에 추가
3-2. for문으로 4방향으로 다시 dfs를 돌려 전진
3-2-1. 만약 maps의 전진하는 방향이 갈 수 있는 길 + 좌표를 벗어나지 않는다면 이전 visited에서 +1
3-3. return 하는 건 거리들이 들어있는 distance

4. 마지막 답으로 return하는 것은 distance의 min
'''

# def dfs (start, end, visited, distance, maps):
#     r, c = start
#     final_r, final_c = end
    
#     if r == final_r and c == final_c:
#         return distance.append(visited[r][c])
    
#     for move_r, move_c in [(1,0),(-1,0),(0,1),(0,-1)]:
#         new_r = r + move_r
#         new_c = c + move_c
#         if 0 <= new_r <= final_r  and 0 <= new_c <= final_c:
#             if maps[new_r][new_c] == 1 and (visited[new_r][new_c] == 0 or visited[new_r][new_c] > visited[r][c] + 1):
#                 visited[new_r][new_c] = visited[r][c] + 1
#                 dfs((new_r, new_c), end, visited, distance, maps)
#                 visited[new_r][new_c] = 0
    


# def solution(maps):
#     answer = 0
#     c = len(maps[0]) -1
#     r = -1
#     for i in maps:
#         r+=1
    
#     visited = [[0] * (c+1) for _ in range (r+1)]
#     visited[0][0] = 1 # 시작 지점 거리 1 설정
#     distance = []
#     start = (0,0)
#     end = (r, c)
    
#     dfs(start, end, visited, distance, maps)
#     print(distance)
#     print(visited)
#     if len(distance) > 0:
#         return min(distance)
#     else:
#         return -1

    
#     return answer

from collections import deque


def solution(maps):
    c = len(maps[0]) -1
    r = len(maps) - 1
    
    start = (0,0)
    end = (r, c)
    
    visited = [[0]*(c+1) for _ in range(r+1)]
    visited[0][0] = 1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    q = deque()
    q.append(start)
    
    while q:
        current_r, current_c = q.popleft()
        
        if (current_r, current_c) == end:
            return visited[current_r][current_c]
        
        for dr, dc in directions:
            next_r = current_r + dr
            next_c = current_c + dc
            
            if 0 <= next_r <= r and 0 <= next_c <= c:
                if maps[next_r][next_c] == 1 and visited[next_r][next_c] == 0:
                    visited[next_r][next_c] = visited[current_r][current_c] + 1
                    q.append((next_r, next_c))
        
    return -1
