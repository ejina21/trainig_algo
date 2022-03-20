def solution(n: int, k: list) -> int:
    t = [0, k[n - 1][0]]
    if n > 1:
        t.append(min(k[n - 2][1], k[n - 1][0] + k[n - 2][0]))
    for i in range(3, n + 1):
        t.append(min(t[i - 1] + k[n - i][0], t[i - 2] + k[n - i][1], t[i - 3] + k[n - i][2]))
    return t[-1]


def main():
    list_check = []
    for i in range(5000):
        list_check.append([1, 1, 1])
    print(solution(5000, list_check))
    print(solution(5, [[5, 10, 15], [2, 10, 15], [5, 5, 5], [20, 20, 1], [20, 1, 1],]))
    print(solution(5, [[5, 10, 15], [2, 10, 15],  [20, 20, 1], [5, 5, 5], [20, 1, 1],]))
    print(solution(5, [[5, 10, 15], [15, 10, 2], [20, 20, 1], [5, 5, 5], [20, 1, 1],]))
    print(solution(3, [[10, 15, 14], [5, 1, 1], [1, 1, 1],]))
    print(solution(1, [[10, 15, 14],]))


if __name__ == '__main__':
    main()