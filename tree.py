class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        self.parent = None
        if children:
            for child in children:
                child.parent = self

    def bfs(self):
        queue = []
        queue.append(self)

        while queue:
            current_node = queue.pop(0)
            print(current_node.value)

            if current_node.children:
                for child in current_node.children:
                    queue.append(child)

    def dfs(self, tree=None):
        if tree is None:
            tree = self

        print(tree.value)

        if tree.children:
            for child in tree.children:
                self.dfs(child)

    def add_node(self, parent_node_value, node):
        parent = self.__find_node(parent_node_value)

        if parent:
            node.parent = parent
            if parent.children is None:
                parent.children = []
            parent.children.append(node)

        return parent

    def remove_node(self, node_value):
        node = self.__find_node(node_value)
        if node:
            parent_node = node.parent
            parent_node.children.remove(node)
            node.parent = None

    def swap_nodes(self, first_node_value, second_node_value):
        first_node = self.__find_node(first_node_value)
        second_node = self.__find_node(second_node_value)

        if first_node and second_node and first_node.parent and second_node.parent:
            first_node_index = self.__get_index(first_node)
            second_node_index = self.__get_index(second_node)

            [first_node.parent.children[first_node_index], second_node.parent.children[second_node_index]] = [
                second_node.parent.children[second_node_index], first_node.parent.children[first_node_index]]

    def __find_node(self, searched_node_value):
        queue = []
        queue.append(self)
        while queue:
            current_node = queue.pop(0)
            if searched_node_value == current_node.value:
                return current_node

            if current_node.children:
                for child in current_node.children:
                    queue.append(child)

        return None

    def __get_index(self, node):
        return node.parent.children.index(node)

if __name__ == '__main__':
    tree = Tree(10, [Tree(5, [Tree(6), Tree(4)]), Tree(15, [Tree(20), Tree(25)])])