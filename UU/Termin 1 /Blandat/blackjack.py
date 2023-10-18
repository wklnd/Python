import random

# Definera kortleken
deck = [
    "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts",
    "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
    "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs",
    "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"
]

# Definera värdet av varje kort
card_values = {
    "Ace of Hearts": 11, "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10,
    "Ace of Diamonds": 11, "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10,
    "Ace of Clubs": 11, "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5, "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10,
    "Ace of Spades": 11, "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10
}

# Definera funktionen för att beräkna handens värde
def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card_values[card] == 11:
            aces += 1
        total += card_values[card]
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

# Definera funktionen för att spela spelet
def play_game():
    # Shuffle the deck
    random.shuffle(deck)
    
    # Deala ut korten
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    # Visa händerna
    print("Player's hand:", player_hand)
    print("Dealer's hand:", [dealer_hand[0], "???"])
    
    # Spelarens tur
    while True:
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == "hit":
            player_hand.append(deck.pop())
            print("Player's hand:", player_hand)
            if calculate_hand(player_hand) > 21:
                print("Bust! Dealer wins.")
                return
        elif choice.lower() == "stand":
            break
    
    # Husets tur
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print("Dealer's hand:", dealer_hand)
    if calculate_hand(dealer_hand) > 21:
        print("Dealer busts! Player wins.")
        return
    
    # Jämför kort
    if calculate_hand(player_hand) > calculate_hand(dealer_hand):
        print("Player wins!")
    elif calculate_hand(player_hand) < calculate_hand(dealer_hand):
        print("Dealer wins!")
    else:
        print("It's a tie!")
        
while True:
    continue_playing = input("Do you want to play a game of blackjack? ")
    if continue_playing.lower() == "y" or "yes": 
        play_game()
    else:
        break
