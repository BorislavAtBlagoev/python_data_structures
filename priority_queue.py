class PriorityQueue:
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

    def dequeue(self):
        last_index = self.size() - 1
        self.__swap(0, last_index)

        removed_value = self.__heap.pop(last_index)

        self.__heapify_down(0)

        return removed_value

    def __heapify_down(self, index):
        left_chield_index = 2 * index + 1
        right_chield_index = 2 * index + 2

        if left_chield_index == 0 or right_chield_index == 0:
            return

        if left_chield_index > self.size() - 1 or right_chield_index > self.size() - 1:
            return

        if self.__heap[left_chield_index] > self.__heap[index]:
            self.__swap(left_chield_index, index)
            self.__heapify_down(left_chield_index)

        if self.__heap[right_chield_index] > self.__heap[index]:
            self.__swap(right_chield_index, index)
            self.__heapify_down(right_chield_index)

    def __heapify(self, index):
        if index == 0:
            return

        parent_index = (index - 1) // 2
        if self.__heap[parent_index] < self.__heap[index]:
            self.__swap(index, parent_index)
            self.__heapify(parent_index)

    def __swap(self, first_index, second_index):
        [self.__heap[first_index], self.__heap[second_index]] = [
            self.__heap[second_index], self.__heap[first_index]]
