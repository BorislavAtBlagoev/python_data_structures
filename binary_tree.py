class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def dfs(self, node=None):
        if not node:
            node = self.root

        print(node.value)

        if node.left:
            self.dfs(node.left)

        if node.right:
            self.dfs(node.right)

    def add(self, value, node=None):
        if not node:
            node = self.root

        if node.value > value:
            if node.left is None:
                node.left = Node(value)
                return
            self.add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                return
            self.add(value, node.right)

    def contains(self, value, node):
        if not node:
            return False

        if node.value == value:
            return True

        if node.value > value:
            return self.contains(value, node.left)
        else:
            return self.contains(value, node.right)

    def search(self, value, node):
        if not node:
            return None

        if node.value == value:
            return node

        if node.value > value:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)

    # def remove(self, value, node=None):
    #     if not node:
    #         node = self.root

    #     if node.left.value == value:
    #         node.left = None
    #         return

    #     if node.right.value == value:
    #         node.right = None
    #         return

    #     if node.value > value:
    #         self.remove(value, node.left)
    #     else:
    #         self.remove(value, node.right)
