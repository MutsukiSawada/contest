# B - Common Raccoon vs Monster

H, N = map(int, input().split())
A = [int(a) for a in input().split()]

for a in A:
    H -= a

print('Yes' if H <= 0 else 'No')
