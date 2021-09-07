def initialize(tree, start, end, list):
    if start >= end:
        return

    middle = (start + end) // 2
    tree.insert(list[middle])
    initialize(tree, start, middle - 1, list)
    initialize(tree, middle + 1, end, list)
