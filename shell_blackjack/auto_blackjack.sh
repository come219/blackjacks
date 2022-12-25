#!/bin/bash


#	bash script to play blackjack

#	review 1:
#	seems to work?

#	review 2:
#	long...

#	review score:
#	7/10



# Blackjack game in Bash

# Create an array representing the deck of cards
# Each element is a rank and suit, separated by a space
deck=(2 spades 3 spades 4 spades 5 spades 6 spades 7 spades 8 spades 9 spades 10 spades J spades Q spades K spades A spades
      2 hearts 3 hearts 4 hearts 5 hearts 6 hearts 7 hearts 8 hearts 9 hearts 10 hearts J hearts Q hearts K hearts A hearts
      2 clubs 3 clubs 4 clubs 5 clubs 6 clubs 7 clubs 8 clubs 9 clubs 10 clubs J clubs Q clubs K clubs A clubs
      2 diamonds 3 diamonds 4 diamonds 5 diamonds 6 diamonds 7 diamonds 8 diamonds 9 diamonds 10 diamonds J diamonds Q diamonds K diamonds A diamonds)

# Shuffle the deck
num_cards=${#deck[@]}
for ((i = 0; i < num_cards; i++)); do
  swap_index=$((RANDOM % num_cards))
  temp=${deck[i]}
  deck[i]=${deck[swap_index]}
  deck[swap_index]=$temp
done

# Initialize player's and dealer's hands
player_hand=()
dealer_hand=()

# Deal the first two cards to the player and the dealer
player_hand+=(${deck[0]})
dealer_hand+=(${deck[1]})
player_hand+=(${deck[2]})
dealer_hand+=(${deck[3]})

# Calculate the player's and dealer's scores
player_score=$(get_hand_value "${player_hand[@]}")
dealer_score=$(get_hand_value "${dealer_hand[@]}")

# Print the player's and dealer's hands and scores
echo "Player's hand: ${player_hand[*]}"
echo "Dealer's hand: ${dealer_hand[*]}"
echo "Player's score: $player_score"
echo "Dealer's score: $dealer_score"

# If the player has blackjack (21 points with just two cards), the player wins.
if [[ "$player_score" -eq 21 ]]; then
  echo "Blackjack! Player wins."
  exit 0
fi

# If the dealer has blackjack, the dealer wins.
if [[ "$dealer_score" -eq 21 ]]; then
  echo "Blackjack! Dealer wins."
  exit 0
fi

# If the player has less than 21 points, the player has the option to hit (draw another card) or stand (keep their current hand)
while [[ "$player_score" -lt 21 ]]; do
  read -p "Hit or stand (h/s)? " choice
  if [[ "$choice" == "h" ]]; then
    player_hand+=(${deck[0]})
    player_score=$(get_hand_value "${player_hand[@]}")
    echo "Player's hand: ${player_hand[*]}"
    echo "Player's score: $player_score"
    if [[ "$player_score" -gt 21 ]]; then
      echo "Bust! Dealer wins."
      exit 0
    fi
  else
    break
  fi
done

# If the dealer has less than 17 points, the dealer has to hit
while [[ "$dealer_score" -lt 17 ]]; do
  dealer_hand+=(${deck[0]})
  dealer_score=$(get_hand_value "${dealer_hand[@]}")
  echo "Dealer's hand: ${dealer_hand[*]}"
  echo "Dealer's score: $dealer_score"
  if [[ "$dealer_score" -gt 21 ]]; then
    echo "Dealer busts! Player wins."
    exit 0
  fi
done

# If neither the player nor the dealer has bust, the higher score wins
if [[ "$player_score" -gt "$dealer_score" ]]; then
  echo "Player wins."
else
  echo "Dealer wins."
fi

# Function to calculate the value of a hand
function get_hand_value() {
  local hand=("$@")
  local value=0
  local num_aces=0
  for card in "${hand[@]}"; do
    rank=${card%% *}
    if [[ "$rank" == "J" || "$rank" == "Q" || "$rank" == "K" ]]; then
      value=$((value + 10))
    elif [[ "$rank" == "A" ]]; then
      value=$((value + 11))
      num_aces=$((num_aces + 1))
    else
      value=$((value + rank))
    fi
  done
  while [[ "$value" -gt 21 && "$num_aces" -gt 0 ]]; do
    value=$((value - 10))
    num_aces=$((num_aces - 1))
  done
  echo "$value"
}

