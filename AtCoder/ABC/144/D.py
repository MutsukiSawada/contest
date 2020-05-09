# D - Water Bottle

from math import atan, pi

a, b, x = map(int, input().split())

theta = 0
if a * a * b / 2 < x:
    theta = atan((2 * ((a ** 2) * b - x)) / (a ** 3))
else:
    theta = atan((a * (b ** 2)) / (2 * x))

print(theta * 180 / pi)
