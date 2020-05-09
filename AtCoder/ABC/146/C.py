# C - Buy an Integer

A, B, X = map(int, input().split())

left = 0
right = 10 ** 9 + 1
while 1 < right - left:
    mid = (left + right) // 2
    ans = A * mid + B * len(str(mid))
    if ans < X:
        left = mid
    elif X < ans:
        right = mid
    else:
        left = mid
        right = mid

print(left)
