from collections import defaultdict


def get_answer(array):
    answ_dict = defaultdict(int)
    for el in array:
        if el:
            answ_dict[el] += 1
    answer = []
    max_value = 0
    for key, value in answ_dict.items():
        if value > max_value:
            answer = [key]
            max_value = value
        elif value == max_value:
            answer.append(key)
    return sorted(answer)


def main():
    array = [el.strip(' []') for el in input().split(',')]
    print(*get_answer(array))


if __name__ == '__main__':
    main()