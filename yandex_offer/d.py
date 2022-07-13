from dataclasses import dataclass


@dataclass
class Arithmetics:
    first_el: int
    diff: int
    id: int


def main():
    n = int(input())
    dict_progressions = {}
    for i in range(n):
        operation = list(map(int, input().split()))
        if operation[0] == 1:
            dict_progressions[operation[3]] = Arithmetics(operation[1], operation[2], operation[3])
        elif operation[0] == 2:
            dict_progressions.pop(operation[1])
        elif operation[0] == 3:
            dict_s = list(sorted(dict_progressions.items(), key=lambda x: (x[1].first_el, x[1].id)))
            print(dict_s[0][1].first_el)
            dict_s[0][1].first_el += dict_s[0][1].diff


def search_min(dict_progressions):
    min_el = None
    arithmetic = None
    for el in dict_progressions.values():
        if not min_el or el.first_el < min_el or (el.first_el == min_el and el.id < arithmetic.id):
            min_el = el.first_el
            arithmetic = el
    arithmetic.first_el += arithmetic.diff
    return min_el


if __name__ == '__main__':
    main()