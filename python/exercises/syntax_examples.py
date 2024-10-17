# S -> aSb
# S -> _
# {a^nb^n}

def analyze_n(word):
    if word == '':
        return True
    else:
        if word.startswith('a') and word.endswith('b'):
            return analyze_n(word[1:-1])
        else:
            return False

# S -> aSa
# S -> bSb
# S -> a
# S -> b
# S -> _

def analyze_palindrome(word):
    if word == '':
        return True
    elif word == 'b':
        return True
    elif word == 'a':
        return True
    elif word.startswith('b') and word.endswith('b'):
        return analyze_palindrome(word[1:-1])
    elif word.startswith('a') and word.endswith('a'):
        return analyze_palindrome(word[1:-1])
    else:
        return False

# a*
# S -> a
# S -> aSa
# S -> _

# a*
# S -> aS
# S -> _

def analyze_kleene(word):
    if word == '':
        return True
    elif word[0] == 'a':
        return analyze_kleene(word[1:])
    else:
        return False

# int x = 6;
# (int, keyword), (x, identifier), (=, operator), (6, integer)
# S -> (keyword_int)(identifier)(operator_=)(S_1)
# S_1 -> integer + S_1
# S_1 -> integer * S_1
# S_1 -> integer - S_1
# S_1 -> integer
# S_1 -> (S_1)

# S -> (f)
# S -> f + S
# S -> f - S
# S -> f * S
# S -> f / S


