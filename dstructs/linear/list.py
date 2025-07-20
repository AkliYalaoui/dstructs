from .linear import Linear
from .nodes import Node
from utils import T
from typing import Optional

class LinkedList(Linear[T]):

    def __init__(self, head: Optional[Node[T]] = None):
        self.head = head
        self.tail = head
        self.__length = 1 if head else 0

    def __len__(self) -> int:
        return self.__length

    def __contains__(self, item: T) -> bool:
        current: Node[T] = self.head

        while current:
            if current.val == item:
                return True
            current = current.nxt

        return False
    
    def __iter__(self) :
        current : Node[T] = self.head
        while current : 
            yield current.val
            current = current.nxt

    def __getitem__(self, index:int) -> T : 
        i  = index if index >= 0 else self.__length + index
        if i < 0  or i >= self.__length:
            raise IndexError(f"Index {i} out of bounds")
        
        current: Node[T] = self.head
        for _ in range(i) : 
            current = current.nxt 

        return current.val

    def insert(self, item: T, index: Optional[int] = -1) -> None:
        i = index if index >= 0 else self.__length + index + 1
        if i < 0 or i > self.__length:
            raise IndexError(f"Index {i} out of bounds")

        node = Node(item)

        # Case: Empty list
        if self.head is None:
            self.head = self.tail = node

        # Case: Insert at head
        elif i == 0:
            node.nxt = self.head
            self.head = node

        # Case: Insert at tail
        elif i == self.__length:
            self.tail.nxt = node
            self.tail = node

        # Case: Insert in middle
        else:
            current = self.head
            for _ in range(i - 1):
                current = current.nxt
            node.nxt = current.nxt
            current.nxt = node

        self.__length += 1

    def remove(self, item: T) -> bool: 
        current: Node[T] = self.head
        previous : Optional[Node[T]] = None
        while current : 
            if current.val == item : 
                if previous is None : 
                    self.head = current.nxt
                else : 
                    previous.nxt = current.nxt
                if current.nxt is None:
                    self.tail = previous
                self.__length -= 1
                return True
            
            previous = current
            current = current.nxt
        
        return False