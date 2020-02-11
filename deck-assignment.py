# Import statements go here


class Deck:
    """
    Simple French Deck class implmented in Python
    """

    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = list('cdhs')

    def __init__(self):
        self._cards = []  # Your code goes inside the listcomp

    def __repr__(self):
        pass

    def __len__(self):
        return len(self._cards)

    def deal(self):
        pass
