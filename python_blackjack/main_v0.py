# Blackjack game in python v0

# Review 1:
# needs error checking

# Review 2:
# possibly better visuals (??)

# Review 3:
# h and s but if not h then always s

# Review score:
# works pretty well 8/10


# Blackjack game in Python

# Import the random module
import random

# Create a list of tuples representing the cards in a deck
# Each tuple consists of a rank and a suit
deck = [
    ('A', 'spades'), ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'), ('7', 'spades'), ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('J', 'spades'), ('Q', 'spades'), ('K', 'spades'),
    ('A', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'), ('9', 'hearts'), ('10', 'hearts'), ('J', 'hearts'), ('Q', 'hearts'), ('K', 'hearts'),
    ('A', 'clubs'), ('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'), ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('J', 'clubs'), ('Q', 'clubs'), ('K', 'clubs'),
    ('A', 'diamonds'), ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds'), ('7', 'diamonds'), ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'), ('J', 'diamonds'), ('Q', 'diamonds'), ('K', 'diamonds')
]

# Shuffle the deck
random.shuffle(deck)

# Initialize player's and dealer's hands
player_hand = []
dealer_hand = []

# Deal the first two cards to the player and the dealer
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Calculate the player's and dealer's scores
player_score = 0
for card in player_hand:
    rank = card[0]
    if rank in ('J', 'Q', 'K'):
        player_score += 10
    elif rank == 'A':
        if player_score + 11 > 21:
            player_score += 1
        else:
            player_score += 11
    else:
        player_score += int(rank)

dealer_score = 0
for card in dealer_hand:
    rank = card[0]
    if rank in ('J', 'Q', 'K'):
        dealer_score += 10
    elif rank == 'A':
        if dealer_score + 11 > 21:
            dealer_score += 1
        else:
            dealer_score += 11
    else:
        dealer_score += int(rank)




# Print the player's and dealer's hands and scores
print("Player's hand: ", player_hand)
print("Dealer's hand: ", dealer_hand)
print("Player's score: ", player_score)
print("Dealer's score: ", dealer_score)

# If the player has blackjack (21 points with just two cards), the player wins.
if player_score == 21:
    print("Blackjack! Player wins.")
    exit()

# If the dealer has blackjack, the dealer wins.
elif dealer_score == 21:
    print("Blackjack! Dealer wins.")
    exit()

# If the player has less than 21 points, the player has the option to hit (draw another card) or stand (keep their current hand)
while player_score < 21:
    choice = input("Hit or stand (h/s)? ")
    if choice == 'h':
        player_hand.append(deck.pop())
        player_score = 0
        for card in player_hand:
            rank = card[0]
            if rank in ('J', 'Q', 'K'):
                player_score += 10
            elif rank == 'A':
                if player_score + 11 > 21:
                    player_score += 1
                else:
                    player_score += 11
            else:
                player_score += int(rank)
        print("Player's hand: ", player_hand)
        print("Player's score: ", player_score)
        if player_score > 21:
            print("Bust! Dealer wins.")
            exit()
    else:
        break

# If the dealer has less than 17 points, the dealer has to hit
while dealer_score < 17:
    dealer_hand.append(deck.pop())
    dealer_score = 0
    for card in dealer_hand:
        rank = card[0]
        if rank in ('J', 'Q', 'K'):
            dealer_score += 10
        elif rank == 'A':
            if dealer_score + 11 > 21:
                dealer_score += 1
            else:
                dealer_score += 11
        else:
            dealer_score += int(rank)
    print("Dealer's hand: ", dealer_hand)
    print("Dealer's score: ", dealer_score)
    if dealer_score > 21:
        print("Dealer busts! Player wins.")
        exit()

# If neither the player nor the dealer has bust, the higher score wins
if player_score > dealer_score:
    print("Player wins.")
else:
    print("Dealer wins.")

