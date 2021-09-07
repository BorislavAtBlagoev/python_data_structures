from binary_tree import Node, BinarySearchTree
from enum import Enum


class Color(Enum):
    BLACK = False
    RED = True


class RedBlackNode(Node):
    def __init__(self, value, left=None, right=None, color=Color.RED.value):
        super().__init__(value, left, right)
        self.color = color


class RedBlackTree(BinarySearchTree):
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(value, self.root)
        self.root.color = Color.BLACK.value

    def print_inorder(self, indent, root):
        if root:
            self.print_inorder(indent + 3, root.right)
            print(f"{' ' * indent}{root.value}{'R' if root.color else 'B'}")
            self.print_inorder(indent + 3, root.left)

    def __insert(self, value, node=None):
        if not node:
            node = RedBlackNode(value)
        elif node.value > value:
            node.left = self.__insert(value, node.left)
        else:
            node.right = self.__insert(value, node.right)

        return self.__rotate(node)

    def __rotate(self, node):
        if self.__is_red(node.left) and self.__is_red(node.left.left):
            node = self.__right_rotation(node)
        if self.__is_red(node.right) and not self.__is_red(node.left):
            node = self.__left_rotation(node)
        if self.__is_red(node.left) and self.__is_red(node.right):
            node = self.__flip_colors(node)

        return node

    @staticmethod
    def __right_rotation(node):
        temp_node = node.left
        node.left = temp_node.right
        temp_node.right = node

        node.color = Color.RED.value
        temp_node.color = Color.BLACK.value

        return temp_node

    @staticmethod
    def __left_rotation(node):
        temp_node = node.right
        node.right = temp_node.left
        temp_node.left = node

        node.color = Color.RED.value
        temp_node.color = Color.BLACK.value

        return temp_node

    @staticmethod
    def __flip_colors(node):
        node.color = Color.RED.value
        node.left.color = Color.BLACK.value
        node.right.color = Color.BLACK.value

        return node

    @staticmethod
    def __is_red(node):
        return node.color if node else False


if __name__ == "__main__":
    tree = RedBlackTree()

    while True:
        command = input()

        if command == "":
            break

        try:
            tree.insert(int(command))
            tree.print_inorder(0, tree.root)
        except ValueError as e:
            print(f"Invalid value: {str(e).split(': ')[1]}")
