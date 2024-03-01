import math

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def maxHeapify(self, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        largest = i
        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def remove(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.maxHeapify(0)
        return root

    def maxHeap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(i)

def sort_movies_batch(names, ratings, name_score_dict):
    max_heap = MaxHeap()
    max_heap.maxHeap(ratings)
    sorted_names = sorted(names, key=lambda x: max_heap.heap.index(name_score_dict[x]))
    return sorted_names


def sort_movies_incre(names, ratings, name_score_dict):
    max_heap = MaxHeap()
    for i in range(len(ratings)):
        max_heap.insert(ratings[i])
    sorted_names = sorted(names, key=lambda x: max_heap.heap.index(name_score_dict[x]))
    return sorted_names

