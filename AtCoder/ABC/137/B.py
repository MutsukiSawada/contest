# B - One Clue

K, X = map(int, input().split())
print(*[x for x in range(X - K + 1, X + K) if -1000000 <= x <= 1000000])
