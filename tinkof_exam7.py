import itertools

n, k = map(int, input().split())

arr = sorted(map(int, input().split()), reverse=True)

answ = list(itertools.combinations(arr, k))

print(len(answ) % (pow(10, 9) + 7))
