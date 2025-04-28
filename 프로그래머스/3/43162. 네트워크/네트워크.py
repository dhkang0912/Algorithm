'''
네트워크의 개수를 센다 => 연결되지 않은 노드를 센다
DFS를 한번 돌리고 그 이후로 방문하지 않은 노드가 있다면 +1을 하면서 센다

1. visited 배열을 노드의 개수만큼 만든다 (n개)
2. for 문을 통해 노드를 DFS 돌린다.
    2-1. 이때 돌리는 조건은 visited 배열에 방문이 안 된 상태일 때 돌린다.
        2-1-1. network를 +1한다.
        2-1-2. DFS에 노드를 넣고 돌린다.
3. network의 개수를 return 한다.

DFS 방문 체크
1. 인자의 노드를 방문 체크한다.
2. for문을 0부터 n-1까지 돈다.
    2-1. 만약 방문 가능한 노드이면
    2-2. DFS를 통해 연결 체크를 한다.
    2-3. DFS임으로 다시 돌아와서 다른 방식으로 방문 가능성이 있는지를 보기 위해 초기화를 한다.

'''
def DFS(node, n, visited, computers):
    visited[node] = 1
    for i in range(n):
        if computers[node][i] == 1 and visited[i] == 0:
            DFS(i, n, visited, computers)

def solution(n, computers):
    visited = [0] * n
    network = 0
    
    for i in range(n):
        if visited[i] == 0:
            network += 1
            DFS(i, n, visited, computers)
    return network
