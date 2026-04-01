from base_heap import BaseHeap, T
from typing import Optional


class MaxHeap(BaseHeap[T]):
    def push(self, val: T) -> None:
        # Impelmentation of push
        self.heap.append(val)
        self.siftUp(len(self.heap) - 1)
        

    def pop(self) -> Optional[T]:
        # Implemenation of pop
        if not self.heap:
            return
        if len(self.heap) == 1:

            return self.heap[0]

        ret = self.heap[0]

        self.heap[0] = self.heap.pop()

        idx = 0
        self.siftDown(idx)
        return ret

    def siftDown(self, idx):

        tempMax = None
        left = self.heap[idx * 2 + 1]
        right = self.heap[idx * 2 + 2]

        current = self.heap[idx]
        if left > right:
            tempMax = idx * 2 + 1
        else:
            tempMax = idx * 2 + 2

        if current < self.heap[tempMax]:
            self.heap[idx], self.heap[tempMax] = self.heap[tempMax], self.heap[idx]
            self.siftDown(tempMax)

    def siftUp(self, idx):

        parent = (idx - 1) // 2

        if self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self.siftUp(parent)

        