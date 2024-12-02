class TennisGame:
    score_dict = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }
    

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
            return
        elif player_name == self.player2_name:
            self.player2_score += 1
            return

    def get_player_score(self, score):
        return self.score_dict.get(score, "Unknown")

    def get_combined_score(self):
        player1_text = self.get_player_score(self.player1_score)
        player2_text = self.get_player_score(self.player2_score)
        return f"{player1_text}-{player2_text}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_endgame_score()
        else:
            return self.get_combined_score()

    def get_even_score(self):
        if self.player1_score < 3:
            return f"{self.get_player_score(self.player1_score)}-All"
        return "Deuce"

    def get_endgame_score(self):
        difference = self.player1_score - self.player2_score
        if difference == 1:
            return f"Advantage {self.player1_name}"
        elif difference == -1:
            return f"Advantage {self.player2_name}"
        elif difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"
