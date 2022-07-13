def try_find(a, b):
    for i in range(4, len(a), 2):
        sr = i // 2
        key1 = f'{a[:sr]}{len(a) - i}{a[len(a) - sr:]}'
        key2 = f'{b[:sr]}{len(b) - i}{b[len(b) - sr:]}'
        if key1 != key2:
            return key1, key2
    else:
        return a, b


def get_answer(array):
    answ_dict = {}
    answer = []
    for el in array:
        key = f'{el[0]}{len(el) - 2}{el[-1]}'
        if key not in answ_dict:
            answ_dict[key] = el
            answer.append(key)
        else:
            a, b = try_find(answ_dict[key], el)
            try:
                index = answer.index(key)
                answer[index] = a
            except ValueError:
                pass
            finally:
                answer.append(b)
    return answer


def main():
    n = int(input())
    array = []
    for i in range(n):
        array.append(input())
    for word in get_answer(array):
        print(word)


if __name__ == '__main__':
    main()