import sys
input = sys.stdin.readline

WB = ['W', 'B']*4
BW = ['B', 'W']*4
white = [WB, BW] * 4
black = [BW, WB] * 4
# print(white)
# print(black)

M, N = map(int, input().split())
arr = [list(input()) for _ in range(M)]
minv = 12434e1332
for row in range(M-8+1):
    for col in range(N-8+1):
        black_minv = 0
        white_minv = 0
        for i in range(8):
            for j in range(8):
                New_row = row + i
                New_col = col + j
                if arr[New_row][New_col] != white[i][j]:
                    black_minv += 1
                if arr[New_row][New_col] != black[i][j]:
                    white_minv += 1

        minv = min(minv, black_minv, white_minv)

print(minv)
