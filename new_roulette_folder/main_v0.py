import random

# Probabilities of the different outcomes in a roulette game
probabilities = {
  "red": 18/38,
  "black": 18/38,
  "green": 2/38
}

def spin_roulette():
  # Spin the roulette and return the outcome
  rand = random.random()
  prob_sum = 0
  for outcome, probability in probabilities.items():
    prob_sum += probability
    if rand < prob_sum:
      return outcome

def play_roulette(bet, amount):
  # Spin the roulette
  result = spin_roulette()

  # Check if the player won or lost
  if result == bet:
    print("You won! The outcome was", result)
    return amount * 2
  else:
    print("You lost. The outcome was", result)
    return 0

def main():
  # Welcome message
  print("Welcome to the roulette game!")

  # Get the player's bet and wager amount
  bet = input("Place your bet (red, black, or green): ")
  while bet not in probabilities:
    print("Invalid bet. Please enter a valid bet (red, black, or green).")
    bet = input("Place your bet (red, black, or green): ")
  amount = int(input("Enter your wager amount: "))

  # Play the game and display the results
  winnings = play_roulette(bet, amount)
  print("You won", winnings, "dollars")

if __name__ == '__main__':
  main()
