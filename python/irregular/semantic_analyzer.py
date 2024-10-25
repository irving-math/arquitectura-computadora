from irregular.tokens import TokenType
from irregular.syntax_analyzer import analyzer as syntax_analyzer
from irregular.lexical_analyzer import analyzer_string as lexical_analyzer

def analyzer(function_set, param_set, tree):
    if type(tree) == tuple:
        analyzer(function_set, param_set, tree[1])
        analyzer(function_set, param_set, tree[2])
    else:
        if tree.token_type == TokenType.IDENTIFIER:
            if tree.word not in param_set:
                raise Exception(f"The param {tree.word} is not defined")


if __name__ == "__main__":
    result = syntax_analyzer(lexical_analyzer("function area base altura = base * profundidad"))
    analyzer(result[0], result[1], result[2])
