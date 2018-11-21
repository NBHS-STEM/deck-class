import random


class Deck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = list('chds')

    def __init__(self):
        self._cards = [rank + suit for rank in self.ranks
                       for suit in self.suits]
        self.shuffle()

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        return 'Deck()'

    def deal(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

