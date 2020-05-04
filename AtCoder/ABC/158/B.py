# B - Count Balls

N, A, B = map(int, input().split())
i = N // (A + B)
j = min(N % (A + B), A)

print(i * A + j)
