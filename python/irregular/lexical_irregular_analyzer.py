from irregular.token import Token
from irregular.token import TokenType

def error(word):
    raise Exception(f"{word} is an invalid token")

def analyzer(word):
    state = 1
    for letter in word:
        if state == 1:
            if letter.isalpha():
                state = 2
            elif letter.isdigit():
                state = 4
            elif letter == '(' or letter == ')':
                state = 7
            elif letter == '+' or letter == '-' or letter == '*' or letter == '/':
                state = 8
            elif letter == '=':
                state = 9
            else:
                error(word)
        elif state == 2:
            if letter.isalpha():
                state = 2
            elif letter == '_':
                state = 3
            else:
                error(word)
        elif state == 3:
            if letter.isalpha():
                state = 2
            else:
                error(word)
        elif state == 4:
            if letter.isdigit():
                state = 4
            elif letter == '.':
                state = 5
            else:
                error(word)
        elif state == 5:
            if letter.isdigit():
                state = 6
            else:
                error(word)
        else:
            error(word)
    if state == 2:
        return Token(word, TokenType.IDENTIFIER)
    elif state == 4 or state == 6:
        return Token(word, TokenType.FLOAT)
    elif state == 7:
        return Token(word, TokenType.PUNCTUATION)
    elif state == 8:
        return Token(word, TokenType.OPERATOR)
    elif state == 9:
        return Token(word, TokenType.EQUAL)
    else:
        error(word)

def analyzer_string(line):
    return []

print(analyzer_string("function area base altura = base * altura"))
