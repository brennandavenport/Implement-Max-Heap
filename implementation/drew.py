from base_heap import BaseHeap, T
from typing import Optional


class MaxHeap(BaseHeap[T]):
    def push(self, val: T) -> None:
        # Impelmentation of push
        self.heap.append(val)
        curr_i = len(self.heap) - 1
        if curr_i == 0:
            return
        # swap with root
        root = self.heap[0]
        self.heap[0] = self.heap[curr_i]
        self.heap[curr_i] = root
        # sift old root back up
        parent_i = (curr_i-1) // 2
        while curr_i != 0 and self.heap[parent_i] < self.heap[curr_i]:
            temp = self.heap[parent_i]
            self.heap[parent_i] = self.heap[curr_i]
            self.heap[curr_i] = temp

            curr_i = parent_i
            parent_i = (curr_i - 1) // 2

       
    def pop(self) -> Optional[T]:
        if len(self.heap) == 0:
            return
        # Implemenation of pop
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return root

    def sift_down(self, index):
        left = 2*index + 1
        right = 2*index + 2
        if len(self.heap) <= left and len(self.heap) <= right: # leaf node
            return
        if len(self.heap) <= right: # has only left child
            if self.heap[index] > self.heap[left]:
                # swap
                temp = self.heap[left]
                self.heap[left] = self.heap[index]
                self.heap[index] = temp
                self.sift_down(left)
            else:
                return
        else: # both children
            if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[index]: 
                temp = self.heap[left]
                self.heap[left] = self.heap[index]
                self.heap[index] = temp
                self.sift_down(left)
            elif self.heap[left] < self.heap[right] and self.heap[right] > self.heap[index]:
                temp = self.heap[right]
                self.heap[right] = self.heap[index]
                self.heap[index] = temp
                self.sift_down(right)
         

        