n = int(input())
R = [int(input()) for _ in range(n)]

mx = -1 * (10 ** 9)
mn = R[0]

for i in range(1, n):
    mx = max(mx, R[i] - mn)
    mn = min(mn, R[i])

print(mx)