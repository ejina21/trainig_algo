def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def heapfi(stones):
    for i in reversed(range(len(stones)//2)):
        heap_sift_down(stones, len(stones), i)

def heap_sift_down(stones, size, i):
    l = left(i)
    r = right(i)
    current = i
    if l < size and stones[l] <= stones[current]:
        current = l
    if r < size and stones[r] <= stones[current]:
        current = r
    if current != i:
        stones[i], stones[current] = stones[current], stones[i]
        heap_sift_down(stones, size, current)

def heap_siftup(stones, index):
    while index > 0 and stones[index] <= stones[parent(index)]:
        stones[index], stones[parent(index)] = stones[parent(index)], stones[index]
        index = parent(index)

def heap_push(stones, el):
    stones.append(el)
    heap_siftup(stones, len(stones) - 1)

def heap_pop(stones):
    el = stones.pop()
    if stones:
        tmp = stones[0]
        stones[0] = el
        heap_sift_down(stones, len(stones), 0)
        return tmp
    return el

def get_energy_for_union(stones, n):
    heapfi(stones)
    points = 0
    for i in range(n - 1):
        new_el = heap_pop(stones) + heap_pop(stones)
        points += new_el
        heap_push(stones, new_el)
    return points

n = int(input())
stones = list(map(int, input().split()))

print(get_energy_for_union(stones, len(stones)))
