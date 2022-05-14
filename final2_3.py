class Guts:
    def __init__(self, character: str):
        self.character: str = character
        self.inside: bool = False
        self.rightspot: bool = False

    def __repr__(self):
        return f"[{self.character} inside: {self.inside} is_in_position: {self.rightspot}]"