/*
*	Java Blackjack v0
*
*/


// Review 1:
// generally works but shows the dealers hand each time..

// Review 2:
// after the first output the cards are shown without the value...

// Review 3: 
// also has the same issue with the python where if not chosen hit (h) then it will stand always..

// Review Score:
// 6/10 bit longer code than python but i guess thats java for you...


import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Blackjack {
    public static void main(String[] args) {
        // Create a deck of cards
        ArrayList<String> deck = new ArrayList<>();
        String[] suits = {"spades", "hearts", "clubs", "diamonds"};
        String[] ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
        for (String suit : suits) {
            for (String rank : ranks) {
                deck.add(rank + " of " + suit);
            }
        }

        // Shuffle the deck
        Collections.shuffle(deck);

        // Initialize player's and dealer's hands
        ArrayList<String> playerHand = new ArrayList<>();
        ArrayList<String> dealerHand = new ArrayList<>();

        // Deal the first two cards to the player and the dealer
        playerHand.add(deck.remove(0));
        dealerHand.add(deck.remove(0));
        playerHand.add(deck.remove(0));
        dealerHand.add(deck.remove(0));

        // Calculate the player's and dealer's scores
        int playerScore = getHandValue(playerHand);
        int dealerScore = getHandValue(dealerHand);

        // Print the player's and dealer's hands and scores
        System.out.println("Player's hand: " + playerHand);
        System.out.println("Dealer's hand: " + dealerHand);
        System.out.println("Player's score: " + playerScore);
        System.out.println("Dealer's score: " + dealerScore);

        // If the player has blackjack (21 points with just two cards), the player wins.
        if (playerScore == 21) {
            System.out.println("Blackjack! Player wins.");
            return;
        }

        // If the dealer has blackjack, the dealer wins.
        if (dealerScore == 21) {
            System.out.println("Blackjack! Dealer wins.");
            return;
        }

        // If the player has less than 21 points, the player has the option to hit (draw another card) or stand (keep their current hand)
        Scanner scanner = new Scanner(System.in);
        while (playerScore < 21) {
            System.out.print("Hit or stand (h/s)? ");
            String choice = scanner.nextLine();
            if (choice.equals("h")) {
                playerHand.add(deck.remove(0));
                playerScore = getHandValue(playerHand);
                System.out.println("Player's hand: " + playerHand);
                System.out.println("Player's score: " + playerScore);
                if (playerScore > 21) {
                    System.out.println("Bust! Dealer wins.");
                    return;
                }
            } else {
                break;
            }
        }

     // If the dealer has less than 17 points, the dealer has to hit
while (dealerScore < 17) {
    dealerHand.add(deck.remove(0));
    dealerScore = getHandValue(dealerHand);
    System.out.println("Dealer's hand: " + dealerHand);
    System.out.println("Dealer's score: " + dealerScore);
    if (dealerScore > 21) {
        System.out.println("Dealer busts! Player wins.");
        return;
    }
}

// If neither the player nor the dealer has bust, the higher score wins
if (playerScore > dealerScore) {
    System.out.println("Player wins.");
} else {
    System.out.println("Dealer wins.");
}

scanner.close();
}

// Method to calculate the value of a hand
public static int getHandValue(ArrayList<String> hand) {
    int value = 0;
    int numAces = 0;
    for (String card : hand) {
        String rank = card.split(" ")[0];
        if (rank.equals("J") || rank.equals("Q") || rank.equals("K")) {
            value += 10;
        } else if (rank.equals("A")) {
            value += 11;
            numAces++;
        } else {
            value += Integer.parseInt(rank);
        }
    }
    while (value > 21 && numAces > 0) {
        value -= 10;
        numAces--;
    }
    return value;
}
}

