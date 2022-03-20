n = int(input())
finish = [['X' for i in range(n)] for j in range(n)]
alph = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n // 2 + n % 2):
    for j in range(n // 2 + n % 2):
        finish[i][j] = alph[(i + j) % len(alph)] if i == 0 or j == 0 else finish[i - 1][j - 1]
        finish[n - i - 1][j] = finish[i][j]
        finish[i][n - j - 1] = finish[i][j]
        finish[n - i - 1][n - j - 1] = finish[i][j]

print('\n'.join([''.join(finish[i]) for i in range(n)]))