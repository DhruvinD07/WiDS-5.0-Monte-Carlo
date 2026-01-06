from blackjack import BlackJack
from cards import Hand

def show_hand(name, hand):
    print(f"{name} (value = {hand.value()}):")
    print(hand)

game = BlackJack()
game.start_round()

while not game.round_over:
    print("\n--- Current Hands ---")
    show_hand("Player", game.player_hand)
    hidden_hand = Hand()
    hidden_hand.add_card(game.dealer_hand.cards[0])
    show_hand("Dealer", hidden_hand)

    choice = input("Hit or Stand? (h/s): ").lower()

    if choice == "h":
        game.player_hit()
    elif choice == "s":
        game.player_stand()
    else:
        print("Invalid choice")

print("\n--- Final Hands ---")
show_hand("Player", game.player_hand)
show_hand("Dealer", game.dealer_hand)

print("\nWinner:", game.winner)