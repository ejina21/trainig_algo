import tracemalloc


def solution(a: int, b: int) -> str:
    stroka = 'YX' * a if a <= b else 'XY' * b
    stroka += 'X' * (a - b) if a >= b else 'Y' * (b - a)
    return stroka


def main():
    tracemalloc.start()
    print(solution(7, 6))
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**3}KB; Peak was {peak / 10**3}KB; Diff = {(peak - current) / 10**3}KB")
    tracemalloc.stop()


if __name__ == '__main__':
    main()
