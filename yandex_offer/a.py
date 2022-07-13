from itertools import product


def hamming(a, b):
    answer = 0
    for i, j in zip(a, b):
        if i != j:
            answer += 1
    return answer


def get_hamm_index(a, b):
    indexes = []
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
            indexes.append(i)
    return answer, indexes


def search_result(a, b, n):
    a = list(a)
    b = list(b)
    result = n
    asnwer = a.copy()
    len_iter, indexes = get_hamm_index(a, b)
    vars = product(range(2), repeat=len_iter)
    for var in vars:
        t = a.copy()
        for i in range(len(indexes)):
            t[indexes[i]] = str(var[i])
        h1 = hamming(a, t)
        h2 = hamming(b, t)
        tmp = max(h1, h2)
        if tmp < result:
            result = tmp
            asnwer = t
    return ''.join(asnwer)


def main():
    n, q = map(int, input().split())
    for i in range(q):
        a, b = input().split()
        print(search_result(a, b, n))


if __name__ == '__main__':
    main()