N = int(input())
for i in range(1, N + 1):
	if i % 3 == 0 or str(i).find('3') != -1:
		print(' ', i, sep='', end = '')
print()