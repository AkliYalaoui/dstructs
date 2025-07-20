from abc import ABC, abstractmethod
from typing import Generic, Optional
from utils import T

class BaseStructure(ABC, Generic[T]) : 
    
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of elements in the structure."""
        pass
    
    @abstractmethod
    def __contains__(self, item : T) -> bool:
        """Check if the structure contains the item."""
        pass
    
    @abstractmethod
    def insert(self, item : T, index : Optional[int] = -1) -> None : 
        """Insert the item at the specified index of the list"""
        pass 

    @abstractmethod
    def remove(self, item : T) -> bool : 
        """Remove the item from the structure."""
        pass
