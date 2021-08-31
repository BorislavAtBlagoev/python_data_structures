class MaxHeap:
    def __init__(self):
        self.__heap = []

    def add(self, value):
        self.__heap.append(value)
        self.__heapify(len(self.__heap) - 1)

    def size(self):
        return len(self.__heap)

    def peek(self):
        return self.__heap[0]

    def print(self):
        print(self.__heap)

    def __heapify(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        if self.__heap[parent_index] < self.__heap[index]:
            [self.__heap[index], self.__heap[parent_index]] = [
                self.__heap[parent_index], self.__heap[index]]
            self.__heapify(parent_index)

