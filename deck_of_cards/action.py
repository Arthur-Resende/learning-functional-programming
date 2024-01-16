import random
import card
import helper


def __shuffle_remaining(shuffled: tuple, remaining: tuple):
    """Recursively shuffles the remaining cards of a deck.

    Args:
        shuffled (tuple): The already shuffled cards.
        remaining (tuple): The remaining cards to be shuffled.

    Raises:
        ValueError: If attempting to shuffle an empty deck.

    Returns:
        tuple: A new tuple representing the selected card and the remaining shuffled deck.
    """
    if not remaining:
        raise ValueError("Can't shuffle an empty deck.")

    if len(remaining) == 1:
        return remaining[0]
    
    index = random.randint(0, len(remaining) - 1)
    selected_card = remaining[index]

    remaining_deck = __shuffle_remaining(
        shuffled=helper.copy_add_item(shuffled, selected_card),
        remaining=helper.copy_remove_index(remaining, index)
    )

    return (selected_card,) + remaining_deck


# a. Shuffle the deck: Implement a function that shuffles the deck randomly.
def shuffle(deck: tuple) -> tuple:
    """Shuffles the given deck of cards.

    Args:
        deck (tuple): A tuple representing a deck of cards.

    Returns:
        tuple: A new tuple representing the shuffled deck.
    """
    return __shuffle_remaining(shuffled=(), remaining=deck)