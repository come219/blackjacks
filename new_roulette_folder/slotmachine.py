import random

# List of possible symbols on the slot machine reels
symbols = ["cherry", "lemon", "apple", "grape", "watermelon"]

def spin_reels():
  # Spin the reels and return a list of symbols
  return [random.choice(symbols) for _ in range(3)]

def play_slot_machine(amount):
  # Spin the reels
  reels = spin_reels()

  # Check if the player won or lost
  if reels[0] == reels[1] == reels[2]:
    print("Jackpot! You won the top prize.")
    return amount * 10
  elif reels[0] == reels[1] or reels[1] == reels[2]:
    print("You won a smaller prize.")
    return amount * 2
  else:
    print("You lost. Better luck next time.")
    return 0

def main():
  # Welcome message
  print("Welcome to the arcade slot machine game!")

  # Get the player's wager amount
  amount = int(input("Enter your wager amount: "))

  # Play the game and display the results
  winnings = play_slot_machine(amount)
  print("You won", winnings, "dollars")

if __name__ == '__main__':
  main()
