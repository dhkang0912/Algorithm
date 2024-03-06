N, M = map(int, input().split())
lst = list(map(int, input().split()))
past_diff = 1243e4213
card_max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = lst[i] + lst[j] + lst[k] # 3개를 뽑고 더한 값
            if card_sum <= M : # 더한 값이 M을 넘으면 안됨
                if card_max_sum < card_sum:
                    card_max_sum = card_sum

print(card_max_sum)


