import itertools
n, k = map(int, input().split())

arr = [i + 1 for i in range(n)]
answ = 0
diff = itertools.permutations(arr)
for i in diff:
    summ = 0
    for j in range(1, n + 1):
        summ += i[j - 1] * j
    if summ % k == 0:
        answ += 1
print(answ)
