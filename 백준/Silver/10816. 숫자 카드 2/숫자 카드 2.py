import sys
input = sys.stdin.readline

N = int(input())
have_cards = list(map(int, input().split()))
have_cards.sort()

M = int(input())
compare_cards = list(map(int, input().split()))

def binary(card, start, end):
    if start > end:
        return 0

    mid = (start+end)//2

    if card == have_cards[mid]:
        return cnt[card]

    elif card < have_cards[mid]:
        return binary(card, start, mid-1)

    else:
        return binary(card, mid+1, end)

cnt = {}
for card in have_cards:
    if card in cnt:
        cnt[card] += 1
    else:
        cnt[card] = 1

# print(cnt)

# while len(compare_cards) > 1:
#     try:
#         print(cnt[compare_cards.pop(0)], end=' ')
#     except:
#         print(0, end=' ')

for card in compare_cards:
    start = 0
    end = len(have_cards) - 1
    result = binary(card, start, end)
    if result == None:
        print(0, end= ' ')
    else:
        print(result, end= ' ')
