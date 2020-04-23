N = int(input())
S = sorted([int(s) for s in input().split()])
Q = int(input())
T = sorted([int(t) for t in input().split()])

cnt = 0
for t in T:
    left = 0
    right = len(S)
    while left < right:
        mid = int((left + right) / 2)
        if t < S[mid]:
            right = mid
        elif S[mid] < t:
            left = mid + 1
        elif t == S[mid]:
            cnt += 1
            break

print(cnt)