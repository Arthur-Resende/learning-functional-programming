import helper


def get_suits() -> tuple:
    """Gets the available Suits."""
    return ("hearts", "diamonds", "clubs", "spades") 


def get_ranks() -> tuple:
    """Gets the available Ranks."""
    return helper.create_sequence(2, 8) + ("jack", "queen", "king", "ace")