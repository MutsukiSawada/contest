# B - Balance

N = int(input())
W = [int(w) for w in input().split()]

mn = float('inf')
for i in range(1, N):
    mn = min(mn, abs(sum(W[:i]) - sum(W[i:])))

print(mn)
