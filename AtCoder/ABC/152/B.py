# B - Comparing Strings

a, b = map(int, input().split())
A = str(a) * b
B = str(b) * a
print(A if A <= B else B)
