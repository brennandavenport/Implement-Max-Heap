from base_heap import BaseHeap, T
from typing import Optional


class MaxHeap(BaseHeap[T]):
    def push(self, val: T) -> None:
        # Impelmentation of push
        self.heap.append(val)

        self.sift_up(len(self.heap) - 1)

    
    def sift_up(self, idx):
        cur = idx
        if cur < 1:
            return 0
        
        if self.heap[cur] > self.sift_up((cur - 1) // 2):
            self.heap[cur], self.heap[(cur - 1) // 2] = self.heap[(cur - 1) // 2], self.heap[cur]

        

            

    def pop(self) -> Optional[T]:
        # Implemenation of pop

        front = self.heap[0]
        self.heap[0] = self.heap[-1]

        self.heap[-1] == -1
        self.sift_down(0)


    
    def sift_down(self, idx):


        if self.heap[idx] == -1:
            return 0
        
        if idx > 2*idx + 1:
            return 0

        if idx > 2*idx + 2:
            return 0

        if idx > len(self.heap) - 1:
            return 0
        
        cur = idx
        
        if self.heap[cur] > self.heap[2*cur + 1]:
            self.heap[cur], self.heap[2*cur + 1] = self.heap[2*cur + 1], self.heap[cur]
            self.sift_down(2*cur + 1)

        if self.heap[cur] > self.heap(2*cur + 2):
            self.heap[cur], self.heap[2*cur + 1] = self.heap[2*cur + 1], self.heap[cur]
            self.sift_down(2*cur + 2)
        
    


        