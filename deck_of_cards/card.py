import rules


def create_card(suit: str, rank: str) -> tuple:
    """Creates a card "object"

    Args:
        suit (str): Suit of the card.
        rank (str): Rank of the card.

    Raises:
        ValueError: Raised if the Suit or the rank is invalid.

    Returns:
        tuple: contains the infomation of the card.
    """
    if suit not in rules.get_suits():
        raise ValueError(f"Invalid suit, the valid suits are {rules.get_suits()}")
    
    if rank not in rules.get_ranks():
        raise ValueError(f"Invalid rank, the valid ranks are {rules.get_ranks()}")

    return (suit, rank)


def get_suit(card: tuple) -> str:
    """Gets the suit value of a specific card.

    Args:
        card (tuple): The card to get information from.

    Returns:
        str: The suit of the card.
    """
    return card[0]


def get_rank(card: tuple) -> str:
    """Gets the Rank of a specific card.

    Args:
        card (tuple): The card to get information from. 

    Returns:
        str: The rank of the card.
    """
    return card[1]


def create_cards_of(suit: str) -> tuple:
    """Creates cards of a specific suit.

    Args:
        suit (str): the suit to create cards of.

    Returns:
        tuple: list of 13 cards from the specified suit.
    """
    return tuple(map(lambda rank: create_card(suit=suit, rank=rank), rules.get_ranks()))


def create_deck() -> tuple:
    """Creates a complete deck of cards"""
    deck_by_suit = tuple(map(lambda suit: create_cards_of(suit), rules.get_suits()))
    return deck_by_suit[0] + deck_by_suit[1] + deck_by_suit[2] + deck_by_suit[3]
