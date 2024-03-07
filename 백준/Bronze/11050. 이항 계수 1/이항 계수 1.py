def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)

N, K = map(int, input().split())
result = facto(N) // (facto(N-K) * facto(K))
print(result)