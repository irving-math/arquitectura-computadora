def automata(word):
    state = 0
    for letter in word:
        if state == 0:
            if letter.isdigit():
                state = 1
            else:
                raise Exception("No es un token")
        elif state == 1:
            if letter.isdigit():
                state = 1
            elif letter == '.':
                state = 2
            else:
                raise Exception("No es un token valido")
        elif state == 2:
            if letter.isdigit():
                state = 3
            else:
                raise Exception("No es un token valido")
        elif state == 3:
            if letter.isdigit():
                state = 3
            else:
                raise Exception("No es un token valido")
        else:
            raise Exception("No es un estado valido")
    if state == 1:
        print(f"La palabra {word} es un numero entero")
    elif state == 3:
        print(f"La palabra {word} es un numero flotante")
    else:
        raise Exception("No es un token valido")

automata("123456789")
automata("123.6")
try:
    automata("15a")
except Exception as e:
    print(e)
try:
    automata("")
except Exception as e:
    print(e)
try:
    automata("98.")
except Exception as e:
    print(e)
