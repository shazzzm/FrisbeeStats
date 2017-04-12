class Point:
    def __init__(self, on_offense, our_score, their_score, our_line):
        self.on_offense = on_offense
        self.our_score = our_score
        self.their_score = their_score
        self.our_line = our_line
        self.passes = []

    def add_pass(self, _pass):
        """
        Adds a pass to the point
        """
        self.passes.append(_pass)

    def set_score(self):
        """
        Sets the last pass as a score
        """
        self.passes[-1].set_score()