n, h, m, k,  = map(int, input().split())

time_half = m // 2
trains = []

for i in range(n):
    _, m1 = map(int, input().split())
    trains.append(m1)

free_time = time_half - k

best_train = [i + 1 for i in range(n)]
best_time = 0
t = 0
for i in range(k):
    bad_trains = []
    for j in range(n):
        if trains[j] not in range(t, t + free_time + 1):
            bad_trains.append(j + 1)
    if len(bad_trains) < len(best_train):
        best_train = bad_trains
        best_time = t
    t += 1

print(len(best_train), best_time)
for el in best_train:
    print(el)