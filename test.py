# n = int(input())
#
# def rec(op, cl, n, s):
# 	if cl == n:
# 		print(s)
# 		return
# 	if op == cl:
# 		rec(op + 1, cl, n, s + '(')
# 	elif op == n:
# 		rec(op, cl + 1, n, s + ')')
# 	else:
# 		rec(op + 1, cl, n, s + '(')
# 		rec(op, cl + 1, n, s + ')')
#
# rec(op=0, cl=0, n=n, s='')

from collections import defaultdict
s1 = input()
s2 = input()

d1 = defaultdict(int)
d2 = defaultdict(int)

for c in s1:
	d1[c] += 1

for c in s2:
	d2[c] += 1

if d1 == d2:
	print(1)
else:
	print(0)