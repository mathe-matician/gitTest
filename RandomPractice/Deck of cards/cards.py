import collections

cards = collections.namedtuple("Cards", ["rank", "suit"])

class FrenchDeck:
  rank = [str(num) for num in range(2, 11)] + list("JQKA")
  suit = "spades clubs diamonds hearts".split()
  
  def __init__(self):
    self._cards = [cards(rank, suit) for rank in self.rank
                                     for suit in self.suit]

  def __len__(self):
    return len(self._cards)
 
  def __getitem__(self, position):
    return self._cards[position]
