class Card:
	"""Represents a standard playing card."""
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s'% (Card.rank_names[self.rank], Card.suit_names[self.suit])


card1 = Card(1,2)

print(card1)
