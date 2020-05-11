# B - Easy Linear Programming / 

A, B, C, K = map(int, input().split())

a = min(A, K)
b = min(B, K - a)
c = min(C, K - a - b)

print(1 * a + b * 0 + c * -1)