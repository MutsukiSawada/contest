# B - Resistors in Parallel

N = int(input())
A = [int(a) for a in input().split()]
dnm = 0
for a in A:
    dnm += 1 / a
print(1 / dnm)
