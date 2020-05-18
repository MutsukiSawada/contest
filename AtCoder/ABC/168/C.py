# C - : (Colon)

import math

A, B, H, M = map(int, input().split())

sub = abs(360 * ((H * 60 + M) / (12 * 60)) - 360 * (M / 60))
deg = min(sub, 360 - sub)
rad = math.radians(deg)

ans = (A ** 2) + (B ** 2) - (2 * A * B * math.cos(rad))

print(ans ** (1 / 2))
