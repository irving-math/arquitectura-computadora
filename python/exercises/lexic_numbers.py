import enum

class TokenType(enum.Enum):
    IDENTIFIER = 0
    KEYWORD = 1
    INTEGER = 2
    FLOAT = 3
    PUNCTUATION = 4
    OPERATOR = 5

class Token:
    token_type = None
    word = None

    def __init__(self, word, token_type):
        self.word = word
        self.token_type = token_type

    def __repr__(self):
        return f"(word={self.word}, type={self.token_type})"

def automata(word):
    state = 0
    for letter in word:
        if state == 0:
            if letter.isdigit():
                state = 1
            elif letter == 'i':
                state = 5
            elif letter == '_' or letter.isalpha():
                state = 4
            elif letter == '(' or letter == ')':
                state = 7
            else:
                raise Exception(f"{word} No es un token")
        elif state == 1:
            if letter.isdigit():
                state = 1
            elif letter == '.':
                state = 2
            else:
                raise Exception(f"{word} No es un token valido")
        elif state == 2:
            if letter.isdigit():
                state = 3
            else:
                raise Exception(f"{word} No es un token valido")
        elif state == 3:
            if letter.isdigit():
                state = 3
            else:
                raise Exception(f"{word} No es un token valido")
        elif state == 4:
            if letter == '_' or letter.isalnum():
                state = 4
        elif state == 5:
            if letter == 'f':
                state = 6
            elif letter == '_' or letter.isalpha():
                state = 4
            else:
                raise Exception(f"{word} No es un token valido")
        else:
            raise Exception(f"{word} No es un estado valido")
    if state == 1:
        return Token(word, TokenType.INTEGER)
    elif state == 3:
        return Token(word, TokenType.FLOAT)
    elif state == 4:
        return Token(word, TokenType.IDENTIFIER)
    elif state == 6:
        return Token(word, TokenType.KEYWORD)
    elif state == 7:
        return Token(word, TokenType.PUNCTUATION)
    else:
        raise Exception(f"{word} No es un token valido")

def lexical_analyzer(text):
    tokens = []
    for word in text.split(" "):
        tokens.append(automata(word))
    return tokens

print(lexical_analyzer(""))
