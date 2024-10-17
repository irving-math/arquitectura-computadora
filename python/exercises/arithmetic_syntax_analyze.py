import enum

class TokenType(enum.Enum):
    FLOAT = 1
    OPERATOR = 2
    PUNCTUATION = 3


class Token:
    word = None
    token_type = None

    def __init__(self, word, token_type):
        self.word = word
        self.token_type = token_type

    def __repr__(self):
        return f"({self.word}, {self.token_type})"

# S -> S + S
# S -> S - S
# S -> S * S
# S -> S / S
# S -> f
# S -> (S)

def analyze_arithmetic_expression(tokens):
    if len(tokens) == 1 and tokens[0].token_type == TokenType.FLOAT:
        return True
    if tokens[0].word == "(" and tokens[-1].word == ")":
        result = analyze_arithmetic_expression(tokens[1:-1])
        if result:
            return True
    if len(tokens) >= 3:
        left_tokens = []
        right_tokens = []
        for element in enumerate(tokens):
            if element[1].token_type != TokenType.OPERATOR:
                left_tokens.append(element[1])
            else:
                right_tokens = tokens[element[0]+1:]
                break
        if not right_tokens:
            return False
        return analyze_arithmetic_expression(left_tokens) and analyze_arithmetic_expression(right_tokens)
    return False

print(analyze_arithmetic_expression([
    Token('(', TokenType.PUNCTUATION),
    Token('3', TokenType.FLOAT),
    Token(')', TokenType.PUNCTUATION),
    Token('+', TokenType.OPERATOR),
    Token('(', TokenType.PUNCTUATION),
    Token('8', TokenType.FLOAT),
    Token(')', TokenType.PUNCTUATION),
]))

