from cards import * 

class BlackJack:
    def __init__(self):
        self.deck = Deck()          
        self.player_hand = Hand()   
        self.dealer_hand = Hand()   
        self.round_over = False     
        self.winner = None           
 
    def start_round(self):
        self.round_over = False
        self.winner = None
        self.player_hand.flush()
        self.dealer_hand.flush()
        self.deck.reset()
        self.deck.shuffle()
        for i in range(2):
            card = self.deck.draw()
            self.player_hand.add_card(card)
            card = self.deck.draw()
            self.dealer_hand.add_card(card)

    def player_hit(self):
        if self.round_over:
            return

        card = self.deck.draw()
        self.player_hand.add_card(card)

        if self.player_hand.value() > 21:
            self.round_over = True
            self.winner = "dealer"

    def player_stand(self):
        if self.round_over:
            return

        self._dealer_play()
        self._compare_hands()
        self.round_over = True

    def _dealer_play(self):
        while self.dealer_hand.value() < 17:
            card = self.deck.draw()
            self.dealer_hand.add_card(card)

        if self.dealer_hand.value() > 21:
            self.winner = "player"

    def _compare_hands(self):
        if self.winner is not None:
            return

        player_value = self.player_hand.value()
        dealer_value = self.dealer_hand.value()

        if player_value > dealer_value:
            self.winner = "player"
        elif dealer_value > player_value:
            self.winner = "dealer"
        else:
            self.winner = "tie"



