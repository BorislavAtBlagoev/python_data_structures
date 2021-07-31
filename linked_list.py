class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            self.head = self.head.next

    def peek(self):
        if self.head:
            return self.head.value


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def enqueue(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node

        if self.last is None:
            self.last = node

        self.last.next = node
        self.last = node

    def dequeue(self):
        self.head = self.head.next
