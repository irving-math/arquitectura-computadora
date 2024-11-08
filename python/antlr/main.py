from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ParseTreeWalker

from antlr.IrregularLexer import IrregularLexer
from antlr.IrregularListener import IrregularListener
from antlr.IrregularParser import IrregularParser


class SemanticListener(IrregularListener):
    parameters = None

    def __init__(self):
        self.parameters = dict()

    def enterEveryRule(self, ctx):
        if hasattr(ctx, 'function_name'):
            children = ctx.getChildren()
            for child in children:
                child.function_name = ctx.function_name

    def enterFunction(self, ctx:IrregularParser.FunctionContext):
        function_name_node = ctx.function_name()
        function_name = function_name_node.getText()
        params_node = ctx.params()
        params_node.function_name = function_name
        exp_node = ctx.expr()
        exp_node.function_name = function_name

    def exitParams(self, ctx:IrregularParser.ParamsContext):
        children = ctx.getChildren()
        params = set()
        for child in children:
            params.add(child.getText())

        self.parameters[ctx.function_name] = params

    def exitIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        if ctx.IDENTIFIER().getText() not in self.parameters[ctx.function_name]:
            raise Exception(f"El parametro {ctx.IDENTIFIER().getText()} no esta definido para {ctx.function_name}")


if __name__ == '__main__':
    code_string = """
function gray_scale red green blue = (red + g + blue)/3
function gray_scale_red r g b = green
"""
    input_stream = InputStream(code_string)
    lexer = IrregularLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IrregularParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    listener = SemanticListener()
    walker.walk(listener, tree)
    # Le indicamos al programa que camine sobre el arbol con el listener dado
