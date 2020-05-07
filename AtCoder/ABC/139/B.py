# B - Power Socket

A, B = map(int, input().split())
i = 0
while (A - 1) * i + 1 < B:
    i += 1
print(i)
