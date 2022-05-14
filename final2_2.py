


class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    VOIDED_LETTER = "*"

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word: str):
        word = word.upper()

        result = [Guts(x) for x in word]

        remaining_secret = list(self.secret)

        # First, check for GREEN letters.
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.inside = True
                remaining_secret[i] = self.VOIDED_LETTER

        for i in range(self.WORD_LENGTH):
            letter = result[i]

            if letter.rightspot:
                continue

            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = self.VOIDED_LETTER
                    letter.inside = True
                    break

        return result

    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
class Guts:
    def __init__(self, character: str):
        self.character: str = character
        self.inside: bool = False
        self.rightspot: bool = False

    def __repr__(self):
        return f"[{self.character} inside: {self.inside} is_in_position: {self.rightspot}]"
