# C - Distinct or Not

N = int(input())
A = [int(a) for a in input().split()]
B = set(A)
print('YES' if len(A) == len(B) else 'NO')
