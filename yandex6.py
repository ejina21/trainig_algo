from collections import defaultdict


class Solution:

    def __init__(self, n, coord, k, frm, to):
        self.n = n
        self.coord = coord
        self.distance = defaultdict(set)
        self.k = k
        self.frm = frm
        self.to = to
        self.count_distance()
        print(self.search_min(1, {self.frm}, set()))

    def count_distance(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                d = 0 if abs(self.coord[i][0] - self.coord[j][0]) + abs(self.coord[i][1] - self.coord[j][1]) > k else 1
                if d:
                    self.distance[i].add(j)
                    self.distance[j].add(i)

    def search_min(self, lvl, next_l, black):
        while True:
            new_set = set()
            for el in next_l:
                if self.distance.get(el):
                    if self.to in self.distance[el]:
                        return lvl
                    new_set.update(self.distance[el])
            black = black.union(next_l)
            next_l = new_set.difference(black)
            if len(next_l) == 0:
                return -1
            lvl += 1


n = input()
n = int(n)
coord_l = []

for i in range(n):
    line = input()
    line = line.split()
    x = int(line[0])
    y = int(line[1])
    coord_l.append((x, y))

k = input()
k = int(k)
line_f = input()
line_f = line_f.split()
frm = int(line_f[0]) - 1
to = int(line_f[1]) - 1

Solution(n, coord_l, k, frm, to)
