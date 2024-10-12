from hand_logic import bestHand
from deck import Deck
from card import Card

def test():
    mydeck = Deck()
    mydeck.shuffle()
    hand = [mydeck.deal_card() for _ in range(2)]
    community = [mydeck.deal_card() for _ in range(5)]
    print('Hand:')
    for card in hand:
        print(card)
    print('Community:')
    for card in community:
        print(card)
    print('Best hand:')
    print(bestHand(hand + community))

def testStraight():
    hand = [Card(14, 'hearts'), Card(2, 'clubs'), Card(3, 'diamonds'), Card(4, 'hearts'), Card(5, 'hearts')]
    print('Hand:')
    for card in hand:
        print(card)
    print('Best hand:')
    print(bestHand(hand))

if __name__ == '__main__':
    testStraight()