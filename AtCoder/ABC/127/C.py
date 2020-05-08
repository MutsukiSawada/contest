# C - Prison

N, M = map(int, input().split())
left = 0
right = 10 ** 5
for _ in range(M):
    l, r = map(int, input().split())
    left, right = max(left, l), min(right, r)

print(len([i for i in range(left, right + 1)]) if left <= right else 0)
