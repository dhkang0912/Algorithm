N, M = map(int, input().split())
if N == M:
    print(N)
    print(M)
else:
    min_value = 1
    i = 2

    while i < max(N, M):
        if N % i == 0 and M % i == 0:
            N //= i
            M //= i
            min_value *= i
            i = 2
        else:
            i+=1

    max_value = min_value * N * M

    print(min_value)
    print(max_value)