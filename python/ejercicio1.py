import re

REG_EXP = re.compile("saluda|((. )+|.+)")


def lexical_analyzer(cadena):
    return REG_EXP.fullmatch(cadena)

def syntax_analyzer(tokens):
    if tokens[0] == 'saluda':
        return tokens[1:]
    else:
        raise "Error sintactico"

def semantic_analyzer(tokens):
    tokens_analizados = []
    for token in tokens:
        if token[0] == '#':
            comando = token[1:]
            if comando == 'cantante':
                tokens_analizados.append('Bad bunny')
            elif comando == 'banda':
                tokens_analizados.append('Arrolladora')
            elif comando == 'prota':
                tokens_analizados.append('Eren Jegger')
            else:
                raise "Error semantico, el token" + comando + " no es una opcion"
        else:
            tokens_analizados.append(token)
    return tokens_analizados

def code_generator(tokens):
    code = ""
    for token in tokens:
        code = code + 'print("Hola " + "' + token + '")\n'
    return code

ejemplo = "saluda irving #cantante"
print(lexical_analyzer(ejemplo))
