W, H, x, y, r = map(int, input().split())

if x + r <= W and y + r <= H and 0 <= x - r and 0 <= y - r:
    print('Yes')
else:
    print('No')