from irregular.syntax_analyzer import analyzer as syntax_analyzer
from irregular.lexical_analyzer import analyzer_string as lexical_analyzer
from irregular.semantic_analyzer import analyzer as semantic_analyzer

def code_generator(function_name, param_set, tree):
    global_code = f"def {function_name}("
    for param in param_set:
        global_code += param + ", "
    if len(param_set) > 0:
        global_code = global_code[:-2]
    global_code += "):\n\treturn "
    global_code += code_exp(tree)
    return global_code

def code_exp(tree):
    if type(tree) == tuple:
        string_left = code_exp(tree[1])
        string_right = code_exp(tree[2])
        return f"({string_left} {tree[0]} {string_right})"
    else:
        return tree.word


if __name__ == "__main__":
    result = syntax_analyzer(lexical_analyzer("function promedio x y = x + y / 2"))
    semantic_analyzer(result[0], result[1], result[2])
    print(code_generator(list(result[0]).pop(), result[1], result[2]))
