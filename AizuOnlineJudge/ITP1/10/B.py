import math

a, b, C = map(float, input().split())

r = math.radians(C)
S = a * b * math.sin(r) / 2
c = ((a ** 2) + (b ** 2) - (2 * a * b * math.cos(r))) ** 0.5
L = a + b + c
h = 2 * S / a

print(S, L, h)