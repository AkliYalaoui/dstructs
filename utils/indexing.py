def normalize_index(index: int, length: int, allow_equal: bool = False) -> int:
    max_allowed = length if allow_equal else length - 1
    i = index if index >= 0 else length + index
    if i < 0 or i > max_allowed:
        raise IndexError(f"Index {i} out of bounds")
    return i