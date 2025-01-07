def toggle(r, c):
    # 3*3 행렬을 뒤집어주기
    for i in range(r, r+3):
        for j in range(c, c+3):
            A[i][j] = not A[i][j]

N, M = map(int,input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
# print(N,M)
# print(A)
# print(B)

cnt = 0
# 시작부터 칸 수를 확인하기 위해 시작+3까지 차지 => N-3까지 가능
# range는 미만이니까 하나 더 큰 기준으로 적기 => N-2
for i in range(N-2):
    for j in range(M-2):
        # 하나씩 지나가며 확인하면서 같지 않다면 3*3으로 뒤집어 주기
        if A[i][j] != B[i][j]:
            toggle(i,j)
            cnt+=1

if A == B:
    print(cnt)
else:
    print(-1)