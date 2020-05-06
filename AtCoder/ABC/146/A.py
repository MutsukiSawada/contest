# A - Can't Wait for Holiday

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
S = str(input())
print(7 - week.index(S) - 1 if S != 'SUN' else 7)
