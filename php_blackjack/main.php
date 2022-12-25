<?php

// define suits and ranks
$suits = array("clubs", "diamonds", "hearts", "spades");
$ranks = array(
    "ace" => 1,
    "2" => 2,
    "3" => 3,
    "4" => 4,
    "5" => 5,
    "6" => 6,
    "7" => 7,
    "8" => 8,
    "9" => 9,
    "10" => 10,
    "jack" => 10,
    "queen" => 10,
    "king" => 10
);

// initialize variables
$player_score = 0;
$dealer_score = 0;
$deck = array();

// build deck
foreach($suits as $suit) {
    foreach($ranks as $rank => $value) {
        $deck[] = array(
            "rank" => $rank,
            "suit" => $suit,
            "value" => $value
        );
    }
}

// shuffle deck
shuffle($deck);

// deal initial cards
$player_hand = array($deck[0], $deck[2]);
$dealer_hand = array($deck[1], $deck[3]);

// calculate initial scores
foreach($player_hand as $card) {
    $player_score += $card['value'];
}
foreach($dealer_hand as $card) {
    $dealer_score += $card['value'];
}

// check if player has a pair
if($player_hand[0]['rank'] == $player_hand[1]['rank']) {
    // prompt player to split pair
    $input = readline("You have a pair of " . $player_hand[0]['rank'] . "s. Split pair (Y/N)? ");
    if(strtolower($input) == "y") {
        // create new hand for second card
        $player_hand_2 = array($player_hand[1]);
        $player_score_2 = $player_hand[1]['value'];
        // remove second card from original hand
        array_pop($player_hand);
        $player_score = $player_hand[0]['value'];
    }
}

// player turn
while($player_score < 21) {
    // display player hand
    echo "Your hand: \n";
    foreach($player_hand as $card) {
        echo $card['rank'] . " of " . $card['suit'] . "\n";
    }
    echo "Your score: " . $player_score . "\n";

    // prompt player to hit or stand
    $input = readline("Hit or stand (H/S)? ");
    if(strtolower($input) == "h") {
        // deal card and add to score
        $player_hand[] = array_shift($deck);
        $player_score += $player_hand[count($player_hand) - 1]['value'];
    } else {
        break;
    }
}

// check if player has busted
if($player_score > 21) {
    echo "You bust!\n";
} else {
    // dealer turn
    echo "Dealer's hand: \n";
    echo $dealer_hand[0]['rank'] . " of " . $dealer_hand[0]['suit'] . " (face-down)\n";
    // check if dealer can peek at face-down card
    if($dealer_hand[1]['value'] == 1 || $dealer_hand[1]['value'] == 10) {
        $input = readline("Dealer's face-down card is an Ace or a 10-valued card. Peek at card (Y/N)? ");
        if(strtolower($input) == "y") {
            echo "Dealer's face-down card: " . $dealer_hand[1]['rank'] . " of " . $dealer_hand[1]['suit'] . "\n";
        }
    }
    while($dealer_score < 17) {
        // deal card and add to score
        $dealer_hand[] = array_shift($deck);
        $dealer_score += $dealer_hand[count($dealer_hand) - 1]['value'];
    }

    // check if dealer has busted
    if($dealer_score > 21) {
        echo "Dealer busts! You win!\n";
    } elseif($player_score > $dealer_score) {
        echo "You win!\n";
    } else {
        echo "You lose!\n";
    }
}


