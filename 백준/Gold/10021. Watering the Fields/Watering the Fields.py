import heapq

# 유클리드 거리 제곱 계산으로 비용 계산
def cost_cal(node_1, node_2):
    x1, y1 = node_1
    x2, y2 = node_2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


# ✅ 프림 알고리즘 (간선 저장 X, 인접 리스트 사용)
def prim(N, C, positions):
    pq = []  # 우선순위 큐 (비용, 노드)
    visited = [False] * N
    total_cost = 0
    cnt = 0

    # ✅ 시작 노드는 0번 인덱스
    heapq.heappush(pq, (0, 0))

    while pq:
        current_cost, node = heapq.heappop(pq)

        # ✅ 이미 방문한 노드는 무시
        if visited[node]:
            continue

        # ✅ 방문 처리 및 비용 추가
        visited[node] = True
        total_cost += current_cost
        cnt += 1

        # ✅ 모든 노드를 방문하면 종료
        if cnt == N:
            return total_cost

        # ✅ 현재 노드와 연결 가능한 노드 탐색 (메모리 절약)
        for next_node in range(N):
            if not visited[next_node]:
                cost = cost_cal(positions[node], positions[next_node])
                if cost >= C:
                    heapq.heappush(pq, (cost, next_node))

    # ✅ 모든 노드를 연결하지 못하면 -1 반환
    return -1


# ✅ 입력 처리
N, C = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(N)]

# ✅ 프림 알고리즘 실행
print(prim(N, C, positions))
