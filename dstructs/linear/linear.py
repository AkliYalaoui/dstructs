from dstructs.base import BaseStructure
from utils import T
from abc import abstractmethod

class Linear(BaseStructure[T]) : 

    @abstractmethod
    def __iter__(self) : 
        """Return an iterator over the elements of the structure."""
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """Get the item at the specified index."""
        pass

    def __repr__(self):
        return repr(list(self))