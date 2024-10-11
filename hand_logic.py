# define functions for each hand to compare

from card import Card

def hasRoyalFlush(hand):
    for suit in ['diamonds', 'hearts', 'clubs', 'spades']:
        if Card(14, suit) in hand and Card(13, suit) in hand and Card(12, suit) in hand and Card(11, suit) in hand and Card(10, suit) in hand:
            return True
    return False

def hasStraightFlush(hand):
    pass

def hasFourOfAKind(hand):
    card_ranks = [card.rank for card in hand]
    for rank in set(card_ranks): # remove duplicates
        if card_ranks.count(rank) == 4:
            return True
    return False

def hasFullHouse(hand):
    card_ranks = [card.rank for card in hand]
    for rank in set(card_ranks): # remove duplicates
        if card_ranks.count(rank) == 3:
            for rank2 in set(card_ranks)-{rank}: # remove duplicates and the first rank used
                if card_ranks.count(rank2) == 2:
                    return True
    return False

def hasFlush(hand):
    card_suits = [card.suit for card in hand]
    for suit in set(card_suits): # remove duplicates
        if card_suits.count(suit) >= 5:
            return True
    return False

def hasStraight(hand):
    card_ranks = list(set(card.rank for card in hand)) # get rid of duplicates
    if 14 in card_ranks: card_ranks.append(1) # account for high/low ace
    card_ranks.sort()
    for i in range(len(card_ranks)-4):
        if card_ranks[i] == card_ranks[i+1]-1 == card_ranks[i+2]-2 == card_ranks[i+3]-3 == card_ranks[i+4]-4:
            return True
    return False

def hasThreeOfAKind(hand):
    card_ranks = [card.rank for card in hand]
    for rank in set(card_ranks): # remove duplicates
        if card_ranks.count(rank) == 3:
            return True
    return False

def hasTwoPair(hand):
    card_ranks = [card.rank for card in hand]
    pairs = 0
    for rank in set(card_ranks): # remove duplicates
        if card_ranks.count(rank) == 2:
            pairs += 1
    return pairs >= 2

def hasPair(hand):
    card_ranks = [card.rank for card in hand]
    for rank in set(card_ranks): # remove duplicates
        if card_ranks.count(rank) == 2:
            return True
    return False


def bestHand(hand):
    if hasRoyalFlush(hand): return 10
    if hasStraightFlush(hand): return 9
    if hasFourOfAKind(hand): return 8
    if hasFullHouse(hand): return 7
    if hasFlush(hand): return 6
    if hasStraight(hand): return 5
    if hasThreeOfAKind(hand): return 4
    if hasTwoPair(hand): return 3
    if hasPair(hand): return 2
    return 1

