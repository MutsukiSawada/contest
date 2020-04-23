# F - Select Half

N = int(input())
A = [int(a) for a in input().split()]

even = 0
odd = 0

for i in range(len(A)):
    if i % 2 == 0: even += A[i]
    if i % 2 != 0: odd += A[i]

print(max(even, odd))