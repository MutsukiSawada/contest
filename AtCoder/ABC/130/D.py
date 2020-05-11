# D - Enough Array

N, K = map(int, input().split())
A = [int(a) for a in input().split()]

right = 1
cnt = 0
k = A[0]
for left in range(N):
    while True:
        if k < K:
            right += 1
            if N < right:
                break
            k += A[right - 1]
        else:
            cnt += N - right + 1
            break
    k -= A[left]

print(cnt)
