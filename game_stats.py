class GameStats:

    def __init__(self, pnw_settings):
        self.pnw_settings = pnw_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.humanscore = 0
        self.compscore = 0

    def human_scores(self):
        self.humanscore += 1

    def comp_scores(self):
        self.compscore += 1

    def human_win(self):
        if self.compscore < self.pnw_settings.points:
            return False
        elif self.compscore >= self.pnw_settings.points:
            return True

    def comp_win(self):
        if self.humanscore < self.pnw_settings.points:
            return False
        elif self.humanscore >= self.pnw_settings.points:
            return True