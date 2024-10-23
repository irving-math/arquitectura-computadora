from irregular.tokens import Token
from irregular.tokens import TokenType

KEYWORD_FUNCTION = 'function'

def error(word):
    raise Exception(f"{word} is an invalid token")

def new_state(letter, current_state):
    expected_letter = current_state - 9 # 10 is the state of the f
    if letter == KEYWORD_FUNCTION[expected_letter]:
        return current_state + 1
    elif letter.isalpha():
        return 2
    elif letter == '_':
        return 3
    else:
        raise Exception(f"{letter} is an invalid letter")

def state_keyword(current_letter, expected_letter, new_state):
    if current_letter == expected_letter:
        return new_state
    elif current_letter.isalpha():
        return 2
    elif current_letter == '_':
        return 3
    else:
        raise Exception(f"{current_letter} is an invalid letter")

def analyzer(word):
    state = 1
    for letter in word:
        if state == 1:
            if letter == 'f':
                state = 10
            elif letter.isalpha():
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
        elif 10 <= state <= 16:
            state = new_state(letter, state)
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
    elif state == 17:
        return Token(word, TokenType.KEYWORD)
    else:
        error(word)

def analyzer_string(line):
    # Agrega espacios extra
    line_with_spaces = []
    for i in range(len(line)):
        if line[i] == '(' or line[i] == ')' or line[i] == '+' or line[i] == '-' or line[i] == '*' or line[i] == '/':
            line_with_spaces.append(' ')
            line_with_spaces.append(line[i])
            line_with_spaces.append(' ')
        else:
            line_with_spaces.append(line[i])
    # Split ignorando espacios multiples
    tokens = []
    buffer = ""
    i = 0
    while i < len(line_with_spaces):
        if line_with_spaces[i] == ' ':
            tokens.append(buffer)
            buffer = ""
            while line_with_spaces[i] == ' ':
                i = i + 1
            continue
        else:
            buffer = buffer + line_with_spaces[i]
        i = i + 1
    tokens.append(buffer)
    real_tokens = []
    for string_list in tokens:
        real_tokens.append(analyzer(string_list))
    return real_tokens

print(analyzer_string("function area base altura = (base * altura)/2"))
