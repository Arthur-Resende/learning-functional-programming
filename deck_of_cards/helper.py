def create_sequence(start: int, size: int) -> tuple:
    """Creates a sequence of numbers.

    Args:
        start (int): number to start the sequence.
        size (int): size of the sequence, a positive integer.
        
    Raises:
        ValueError: Raised if size is not positive.

    Returns:
        tuple: tuple containing sequence of numbers
    """
    if size < 0:
        raise ValueError("Size must be non-negative.")

    if size == 0:
        return (start,)
    
    next_value = start + size
    return create_sequence(start, size - 1) + (next_value,)


def copy_add_item(original_tuple: tuple, new_item) -> tuple:
    """Creates a new tuple by adding a new item to the original tuple.

    Args:
        original_tuple (tuple): The original tuple.
        new_item: The item to add to the tuple.

    Returns:
        tuple: A new tuple containing the elements of the original tuple and the new item.
    """
    return original_tuple + (new_item,)


def copy_remove_index(original_tuple: tuple, index: int) -> tuple:
    """Creates a new tuple by removing an element at the specified index from the original tuple.

    Args:
        original_tuple (tuple): The original tuple.
        index (int): The index to remove.

    Raises:
        IndexError: If the index is out of bounds (negative or greater than or equal to the tuple length).

    Returns:
        tuple: A new tuple with the specified element removed.
    """
    if index < 0 or index >= len(original_tuple):
        raise IndexError(f"Index {index} is out of bounds. Valid range: 0 to {len(original_tuple) - 1}.")

    return original_tuple[:index] + original_tuple[index + 1:]
