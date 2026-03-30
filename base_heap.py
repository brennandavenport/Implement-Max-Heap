from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class BaseHeap(ABC, Generic[T]):
    def __init__(self):
        self.heap: list[T] = []

    def __len__(self) -> int:
        return len(self.heap)

    @abstractmethod
    def push(self, val: T) -> None:
        # add element to heap
        pass 

    @abstractmethod
    def pop(self) -> Optional[T]:
        # remove the root from the heap
        # This value should be the max in the array
        pass 

    @property
    def peek(self) -> Optional[T]:
        return self.heap[0] if self.heap else None
