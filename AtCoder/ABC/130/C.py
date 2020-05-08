# C - Rectangle Cutting

W, H, x, y = map(int, input().split())
print(max(W, H) * min(W, H) / 2, 1 if W == x * 2 and H == y * 2 else 0)
