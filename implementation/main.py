from base_heap import BaseHeap, T
from typing import Optional


class MaxHeap(BaseHeap[T]):

    def in_bounds(self, index: int):
        return True if index >= 0 and index < len(self.heap) else False
    
    def push(self, val: T) -> None:
        # Impelmentation of push
        self.heap.append(val) # add to end of heap
        self.sift_up(len(self.heap) - 1) # sort
        return
    
    def pop(self) -> Optional[T]:
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] # replace root with last element in heap
        self.heap.pop()
        self.sift_down(0)
        return max_val


    def sift_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index != 0 and self.heap[parent] < self.heap[index]: # if parent is smaller, swap
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.sift_up(parent)
        else:
            return

    def sift_down(self, index: int) -> None:
        left_child = 2*index + 1
        right_child = 2*index + 2
        if not self.in_bounds(left_child) and not self.in_bounds(right_child):
            return
        largest = index # Assume parent is the largest
        if self.in_bounds(left_child) and self.heap[left_child] > self.heap[largest]: # if left child is larger, update value
            largest = left_child
        if self.in_bounds(right_child) and self.heap[right_child] > self.heap[largest]: # if right child is larger, update value
            largest = right_child
        if largest != index: # If we have a new largest value
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.sift_down(largest)