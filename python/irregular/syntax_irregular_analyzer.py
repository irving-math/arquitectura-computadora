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

def analyze_arithmetic(tokens):
    term = parse_term(tokens)
    if tokens:
        if tokens[-1].token_type == TokenType.OPERATOR and (tokens[-1].word == '+' or tokens[-1].word == '-'):
            operator = tokens.pop()
            return (operator, analyze_arithmetic(tokens), term)
        else:
            raise Exception(f'Unexpected token: {tokens[0]}, expected "+" or "-"')
    else:
        return term

def parse_term(tokens):
    pass

def parse_factor(tokens):
    pass







print(analyze_parameters([
    Token(word='hola', token_type=TokenType.IDENTIFIER),
    Token(word='3', token_type=TokenType.FLOAT),
    Token(word='hello', token_type=TokenType.IDENTIFIER),
    Token(word='=', token_type=TokenType.EQUAL),
    Token(word='3', token_type=TokenType.FLOAT),
]))