import enum

class TokenType(enum.Enum):
    FLOAT = 1
    OPERATOR = 2
    PUNCTUATION = 3
    IDENTIFIER = 4
    KEYWORD = 5
    EQUAL = 6

class Token:
    word = None
    token_type = None

    def __init__(self, word, token_type):
        self.word = word
        self.token_type = token_type

    def __repr__(self):
        return f"('{self.word}', {self.token_type})"