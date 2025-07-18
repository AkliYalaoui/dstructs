from dataclasses import dataclass
from dstructs.base import BaseStructure
from utils import T
from typing import Generic, Optional

@dataclass
class Node(Generic[T]) : 
    val : T
    nxt : Optional['Node[T]'] = None


class LinkedList(BaseStructure[T]):

    def __init__(self, head: Optional[Node[T]] = None) : 
        self.head = head
        self.tail = head
        self.__length = 1 if head else 0

    def __len__(self) -> int:
        return self.__length
    
    def __contains__(self, item: T) -> bool:
        current = self.head 

        while current : 
            if current.val == item : 
                return True 
            current = current.nxt
        
        return False
    
    def insert(self, item : T, index : Optional[int] = -1) -> None:
        node = Node(item)
        if not self.head : 
            self.head = self.tail = node 

        else : 
            self.tail.nxt = node 
            self.tail = node

        self.__length += 1