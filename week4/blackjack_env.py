from blackjack import BlackJack

class BlackJackEnv:
    def __init__(self):
        self.game = BlackJack()

    def reset(self):
        self.game.start_round()
        return self._get_state()

    def step(self, action):
        # action: 0 = Stick, 1 = Hit
        if action == 1:
            self.game.player_hit()
        else:
            self.game.player_stand()

        done = self.game.round_over
        reward = 0

        if done:
            if self.game.winner == "player":
                reward = 1
            elif self.game.winner == "dealer":
                reward = -1
            else:
                reward = 0

        return self._get_state(), reward, done

    def _get_state(self):
        player_sum = self.game.player_hand.value()
        dealer_upcard = self._dealer_upcard()
        usable_ace = self._usable_ace()
        return (player_sum, dealer_upcard, usable_ace)

    def _dealer_upcard(self):
        card = self.game.dealer_hand.cards[0]
        if card.rank in ["J", "Q", "K"]:
            return 10
        elif card.rank == "A":
            return 1
        else:
            return int(card.rank)

    def _usable_ace(self):
        total = 0
        aces = 0
        for card in self.game.player_hand.cards:
            if card.rank == "A":
                aces += 1
                total += 11
            elif card.rank in ["J", "Q", "K"]:
                total += 10
            else:
                total += int(card.rank)
        return aces > 0 and total <= 21
