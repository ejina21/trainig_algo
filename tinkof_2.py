def solution(n: int, k: int, path: str) -> str:
    sum_zero = 0
    for i in range(1, n):
        if path[i] == '0':
            sum_zero += 1
            if sum_zero >= k:
                return 'NO'
        else:
            sum_zero = 0
    return 'YES'


def main():
    print(solution(5, 2, '10101'))
    print(solution(8, 4, '11000011'))


if __name__ == '__main__':
    main()