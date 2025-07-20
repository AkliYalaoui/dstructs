from dataclasses import dataclass
from utils import T
from typing import Generic, Optional


@dataclass
class Node(Generic[T]):
    val: T
    nxt: Optional['Node[T]'] = None