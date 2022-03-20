import math
from collections import defaultdict
import random


def solution2(n: int, k: list) -> list:
    max_gcd = max(k)
    k.remove(max_gcd)
    fin_list = [max_gcd]
    f_dict = defaultdict(list)
    for i in k:
        f_dict[math.gcd(max_gcd, i)].append(i)
    f_res = sorted(f_dict.items(), key=lambda x: x[0], reverse=True)
    print(f_res)
    fin_list += [v for val in f_res for v in val[1]]
    return fin_list


def solution(n: int, k: list) -> list:
    max_gcd = max(k)
    k.remove(max_gcd)
    fin_list = [max_gcd]
    i = 1
    while i < n:
        ind, max_gcd = search_max(max_gcd, k)
        print(f'{max_gcd} - {k[ind]}')
        if max_gcd == 1:
            fin_list += k
            break
        fin_list.append(k.pop(ind))
        i += 1
    return fin_list


def search_max(key, k):
    max_gcd = 1
    ind = -1
    for i in range(len(k)):
        gcd = math.gcd(key, k[i])
        if gcd > max_gcd:
            ind = i
            max_gcd = gcd
    return ind, max_gcd


def main():
    # for i in range(20):
        # lst = []
        # for _ in range(10):
        #     lst.append(random.randint(1, 100))
        # print(f'list={lst}')
        # print(solution(10, lst[:]))
        # print(solution2(10, lst))
        # print('----------------------------')
    # print(solution(6, [96, 128, 88, 80, 52, 7]))
    # print(solution(10, [59, 95, 76, 17, 6, 45, 80, 40, 6, 100]))
    print(solution(10, [95, 88, 76, 42, 96, 79, 1, 48, 44, 66]))
    print(solution2(10, [95, 88, 76, 42, 96, 79, 1, 48, 44, 66]))

    # print(solution2(10, [21, 99, 42, 75, 100, 84, 79, 34, 38, 22]))


# list=[95, 88, 76, 42, 96, 79, 1, 48, 44, 66]
# [96, 48, 88, 76, 44, 42, 66, 95, 79, 1]
# [96, 48, 88, 42, 66, 76, 44, 95, 79, 1]


if __name__ == '__main__':
    main()