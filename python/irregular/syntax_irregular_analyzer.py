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
    i = 0
    parenthesis_count = 0
    while i < len(tokens) and (parenthesis_count != 0 or (tokens[i].word != '+' and tokens[i].word != '-' )):
        if tokens[i].word == '(':
            parenthesis_count += 1
        if tokens[i].word == ')':
            parenthesis_count -= 1
        i += 1
    if i == len(tokens):
        return analyze_term(tokens)
    elif i == len(tokens) - 1 or i == 0:
        raise Exception(f'Operator + or - without a term')
    else:
        return tokens[i].word, analyze_term(tokens[:i]), analyze_exp(tokens[i + 1:])

def analyze_term(tokens):
    i = 0
    parenthesis_count = 0
    while i < len(tokens) and (parenthesis_count!= 0 or (tokens[i].word != '*' and tokens[i].word != '/')):
        if tokens[i].word == '(':
            parenthesis_count += 1
        if tokens[i].word == ')':
            parenthesis_count -= 1
        i += 1
    if i == len(tokens):
        return analyze_factor(tokens)
    elif i == len(tokens) - 1 or i == 0:
        raise Exception(f'Operator * or / without a term')
    else:
        return tokens[i].word, analyze_factor(tokens[:i]), analyze_term(tokens[i + 1:])

def analyze_factor(tokens):
    if tokens[0].word == '(':
        if tokens[-1].word == ')':
            return analyze_exp(tokens[1:-1])
        else:
            raise Exception(f'( without a close -> )')
    else:
        if tokens[0].token_type == TokenType.IDENTIFIER or tokens[0].token_type == TokenType.FLOAT:
            return tokens[0].word
        else:
            raise Exception(f'Unexpected token: {tokens[0]}, expected a float or identifier')




print(analyze_exp([
    Token(word='(', token_type=TokenType.PUNCTUATION),
    Token(word='3', token_type=TokenType.FLOAT),
    Token(word='*', token_type=TokenType.OPERATOR),
    Token(word='8', token_type=TokenType.FLOAT),
    Token(word=')', token_type=TokenType.PUNCTUATION),
    Token(word='+', token_type=TokenType.OPERATOR),
    Token(word='hola', token_type=TokenType.FLOAT),
]))