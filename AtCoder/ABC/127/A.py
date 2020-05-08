# A - Ferris Wheel

A, B = map(int, input().split())
print(B if 13 <= A else B // 2 if 6 <= A <= 12 else 0)
