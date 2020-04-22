x1, y1, x2, y2 = map(float, input().split())
w, h = abs(x1 - x2), abs(y1 - y2)
print(h if w == 0 else w if h == 0 else (w ** 2 + h ** 2) ** 0.5)