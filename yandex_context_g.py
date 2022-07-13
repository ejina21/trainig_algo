class Node:
    def __init__(self, weight, parent) -> None:
        self.weight = weight
        self.parent = parent
        self.children = []
        self.touch = False
        self.sum = 0


def get_number_of_upgoing_paths(root, x):
    stack = [root]
    pre_sum_dict = {}
    pre_sum_dict[0] = 1
    count = 0
    current_sum = 0
    while stack:                            #      1       0:1  1:1 2:1  4:0 3:1
        node = stack[-1]                    #    1   1
        if not node.touch:                  #  1       2
            current_sum += node.weight      # 1
            node.sum = current_sum
            node.touch = True

            if current_sum - x in pre_sum_dict:
                count += pre_sum_dict.get(current_sum - x)
            if current_sum not in pre_sum_dict:
                pre_sum_dict[current_sum] = 0

            pre_sum_dict[current_sum] = pre_sum_dict.get(current_sum) + 1

        if node.children:
            child = node.children.pop()
            stack.append(child)
            continue
        current_sum -= node.weight
        pre_sum_dict[node.sum] = pre_sum_dict.get(node.sum) - 1
        stack.pop()
    return count


def read_tree(tree_size: int):
    nodes = []
    root = None
    for i in range(tree_size):
        p, w = map(int, input().split())
        nodes.append(Node(w, p))
        if p == -1:
            root = nodes[i]
    for i in range(tree_size):
        if nodes[i].parent != -1:
            nodes[nodes[i].parent].children.append(nodes[i])
    return root

n, x = map(int, input().split())
root = read_tree(n)
print(get_number_of_upgoing_paths(root, x))
