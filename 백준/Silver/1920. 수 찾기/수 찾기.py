import sys
input = sys.stdin.readline

N = int(input())
N_numbers = set(map(int, input().split()))
# min_N_numbers = min(N_numbers)
# max_N_numbers = max(N_numbers)

M = int(input())
M_numbers = list(map(int, input().split()))

for i in range(M):
    if M_numbers[i] not in N_numbers:
        print(0)
    else:
        print(1)