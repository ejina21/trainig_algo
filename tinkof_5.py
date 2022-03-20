import time


def solution(h: int, w: int, n: int, w_list: list) -> list:
    free_list = [w] * h
    answ_list = []
    for el in w_list:
        flag = True
        for i, line in enumerate(free_list):
            if line - el >= 0:
                answ_list.append(i + 1)
                free_list[i] = line - el
                flag = False
                break
        if flag:
            answ_list.append(-1)
    return answ_list


def main():
    print(time.time())
    solution(100, 6, 6, [5, 3, 2, 1, 5, 4])
    print(time.time())


if __name__ == '__main__':
    main()