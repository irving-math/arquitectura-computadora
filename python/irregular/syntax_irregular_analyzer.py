from irregular.tokens import TokenType, Token

functions_set = set()


def analyzer(tokens):
    token = tokens.pop(0)
    if token.token_type != TokenType.KEYWORD:
        raise Exception(f'Unexpected token: {token}, expected "function"')
    token = tokens.pop(0)

    if token.token_type != TokenType.IDENTIFIER:
        raise Exception(f'Unexpected token: {token}, expected a function name identifier')
    functions_set.add(token.word)

    parameters = analyze_parameters(tokens)
    expresion = analyze_arithmetic(tokens)


def analyze_parameters(tokens):
    if tokens:
        token = tokens.pop(0)
        if token.token_type != TokenType.EQUAL:
            if token.token_type == TokenType.IDENTIFIER:
                return [token.word] + analyze_parameters(tokens)
            else:
                raise Exception(f'Unexpected token: {token}, expected a parameter identifier')
        else:
            return []
    else:
        return []

def analyze_exp(tokens):
    term = analyze_term(tokens)
    if tokens:
        if tokens[-1].token_type == TokenType.OPERATOR and (tokens[-1].word == '+' or tokens[-1].word == '-'):
            operator = tokens.pop()
            return (operator, analyze_exp(tokens), term)
        else:
            raise Exception(f'Unexpected token: {tokens[-1]}, expected "+" or "-"')
    else:
        return term

def analyze_term(tokens):
    factor = analyze_factor(tokens)
    if tokens:
        if tokens[-1].token_type == TokenType.OPERATOR and (tokens[-1].word == '*' or tokens[-1].word == '/'):
            operator = tokens.pop()
            return (operator, analyze_term(tokens), factor)
        else:
            raise Exception(f'Unexpected token: {tokens[-1]}, expected "*" or "/"')
    else:
        return factor

def analyze_factor(tokens):
    i = len(tokens) - 1
    while i > 0 and tokens[i] != '*' and tokens[i] != '/':
        i = i - 1
    if i == 0:
        if tokens[i] == '*' or tokens[i] == '/':
            raise Exception(f'Tokens: {tokens}, starts with "*" or "/"')
        else:
           new_tokens = tokens[:]
           tokens.clear()
    else:
        tokens = tokens[:i+1]
        new_tokens = tokens[i+1:]
    if len(new_tokens) == 1 and (
            new_tokens[0].token_type == TokenType.IDENTIFIER or new_tokens[0].token_type == TokenType.FLOAT
    ):
        return new_tokens[0].word
    elif new_tokens[0] == '(' and new_tokens[-1] == ')':
        return analyze_exp(new_tokens[1:-1])

    else:
        raise Exception(f'Unexpected tokens: {tokens}')



print(analyze_exp([
    Token(word='2', token_type=TokenType.FLOAT),
    Token(word='+', token_type=TokenType.FLOAT),
    Token(word='3', token_type=TokenType.FLOAT),
]))