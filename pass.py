import enum

class TurnoverReason(enum.Enum):
    THROWER_ERROR = 1
    RECEIVER_ERROR = 2

class Pass:
    def __init__(self, player_from, player_to, score):
        self.player_from = player_from
        self.player_to = player_to
        self.score = score
        self.turnover_reason = None

    def set_turnover(self, turnover_reason):
        """
        If the pass isn't completed, call this with a reason why
        (receiver error/thrower error)
        """
        self.turnover_reason = turnover_reason