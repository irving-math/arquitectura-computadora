from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from antlr.ArithmeticLexer import ArithmeticLexer
from antlr.ArithmeticParser import ArithmeticParser

if __name__ == '__main__':
    code_string = '(3 * 3 )'
    input_stream = InputStream(code_string)
    lexer = ArithmeticLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.program()
    print(tree.toStringTree())
