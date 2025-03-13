'''
작업

X 작업을 끝내기 위해 해야하는 작업의 개수
bfs, dfs 둘 다 가능
visited로 X 작업 방문 순서를 구하면 됨

# 입력
1. 작업 개수 = n / 작업 순서의 개수 = m
2. m개 만큼 반복하며 노드 연결 관계를 추가
    - 작업 순서가 위배되는 적이 없으니 방향이 있음
    - x, y => x 작업 이후 y 작업 = y -> x 방향
3. m개 이후 오늘 끝내야 하는 작업 X = 여기까지 걸리는 순서
'''
import sys 
input = sys.stdin.readline

def dfs(node):
    stack = []
    stack.append(node)
    visited[node] = 1

    while stack:
        n = stack.pop()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
    

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 0 사용 안함
visited[0] = 1
for i in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

# print(graph)
target = int(input())
dfs(target)
print(sum(visited)-2)


