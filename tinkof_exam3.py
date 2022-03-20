n = input()
count = 0
index = 0
for i in range(len(n) - 1, 0, -1):
    if n[i] != '0':
        index = i
        break
for i in range(index):
    if n[i] == '0':
        count += 1
print(count)