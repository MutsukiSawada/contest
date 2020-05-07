# B - Roller Coaster

N, K = map(int, input().split())
print(len([h for h in map(int, input().split()) if K <= h]))
