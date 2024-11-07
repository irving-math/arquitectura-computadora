from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ParseTreeWalker

from antlr.IrregularLexer import IrregularLexer
from antlr.IrregularListener import IrregularListener
from antlr.IrregularParser import IrregularParser


class SemanticListener(IrregularListener):
    parameters = None

    def __init__(self):
        self.parameters = set()

    def exitParams(self, ctx:IrregularParser.ParamsContext):
        children = ctx.getChildren()
        for child in children:
            self.parameters.add(child.getText())
        print(self.parameters)

    def exitIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        param = ctx.IDENTIFIER().getText()
        if param not in self.parameters:
            raise Exception(f"{param} is not defined as a parameter")


if __name__ == '__main__':
    code_string = 'function gray_scale r g b = (f + g + b)/3'
    input_stream = InputStream(code_string)
    lexer = IrregularLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IrregularParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    listener = SemanticListener()
    walker.walk(listener, tree) # Le indicamos al programa que camine sobre el arbol con el listener dado
