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
