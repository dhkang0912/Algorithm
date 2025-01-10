def binary_search(s, e, target):
    while s <= e:
        mid = (s+e)//2
        if w[mid] == target:
            return True
        elif w[mid] > target:
            e = mid -1
        else:
            s = mid +1
    return False


def check(N, C):
    global success
    # 한번에 찾을 수 있는 경우
    if C in w :
        success = 1
        return
    # 가능한 인덱스 범위
    i, j = 0, N-1

    while i < j:
        # 두개를 가지고 더해서 찾을 수 있는 경우
        # 양 끝단을 더하고, 뒤에서부터 작아지는 수를 더 해가면서 조건을 확인
        sum = w[i] + w[j]
        if sum > C:
            j-=1
        elif sum == C:
            success = 1
            return
        # 세개를 더해야만 찾을 수 있는 경우
        else:
            diff = C - sum
            if w[i] != diff and w[j] != diff and binary_search(i, j, diff):
                success = 1
                return
            i+=1

N, C = map(int, input().strip().split())
w = list(map(int, input().strip().split()))
w.sort()
success = 0

check(N,C)
print(success)