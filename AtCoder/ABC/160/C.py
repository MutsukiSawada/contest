# C - Traveling Salesman around Lake

K, N = map(int, input().split())
A = [a for a in map(int, input().split())]

total = 0
mx = 0

for i in range(N):
    if i == N - 1:
        dist = K - A[i] + A[0]
    else:
        dist = A[i + 1] - A[i]
    if mx < dist:
        mx = dist
    total += dist

print(total - mx)
