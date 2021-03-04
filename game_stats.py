class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False
        self.high_score = self._get_high_score()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def save_high_score(self,high_score):
        high_score = str(high_score)
        with open("high_score.txt",'w') as f:
            f.write(high_score)
            
    def _get_high_score(self):
        with open("high_score.txt") as f:
            sc = f.read()
        return int(sc)


    