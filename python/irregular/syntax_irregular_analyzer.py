from irregular.token import TokenType

def analyzer(tokens):
    if (tokens[0].token_type == TokenType.KEYWORD
        and tokens[1].token_type == TokenType.IDENTIFIER
        ):
        parameters = []
        arithmetic = []
        for token in tokens[2:]:
            if token.token_type == TokenType.EQUAL:
                break
            else:
                parameters.append(token)
        #TODO: Agregar a la lista arithmetic lo que queda despues del igual

def analyze_parameters(tokens):
    pass

def analyze_arithmetic(tokens):
    pass