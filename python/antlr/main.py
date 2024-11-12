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
        if hasattr(ctx, 'my_function_name'):
            children = ctx.getChildren()
            for child in children:
                child.my_function_name = ctx.my_function_name

    def enterFunction(self, ctx:IrregularParser.FunctionContext):
        function_name_node = ctx.function_name()
        function_name = function_name_node.getText()
        params_node = ctx.params()
        params_node.my_function_name = function_name
        exp_node = ctx.expr()
        exp_node.my_function_name = function_name

    def exitParams(self, ctx:IrregularParser.ParamsContext):
        children = ctx.getChildren()
        params = set()
        for child in children:
            params.add(child.getText())

        self.parameters[ctx.my_function_name] = params

    def exitIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        if ctx.IDENTIFIER().getText() not in self.parameters[ctx.my_function_name]:
            raise Exception(f"El parametro {ctx.IDENTIFIER().getText()} no esta definido para {ctx.my_function_name}")

class CodeGeneratorListener(IrregularListener):

    def exitProgram(self, ctx:IrregularParser.ProgramContext):
        ctx.code = ""
        for f in ctx.getChildren():
            if not f.getText() == '<EOF>':
                ctx.code += f.code + "\n"

    def exitFunction(self, ctx:IrregularParser.FunctionContext):
        function_name = ctx.function_name().getText()
        param_names = []
        for param in ctx.params().getChildren():
            param_names.append(param.getText())
        param_with_comma = ', '.join(param_names)
        ctx.code = f"def {function_name}({param_with_comma}):\n"
        ctx.code += "\treturn " + ctx.expr().code

    def exitFloatOnly(self, ctx:IrregularParser.FloatOnlyContext):
        ctx.code = ctx.FLOAT().getText()

    def exitParenthesis(self, ctx:IrregularParser.ParenthesisContext):
        ctx.code = "(" + ctx.expr().code + ")"

    def exitIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        ctx.code = ctx.IDENTIFIER().getText()

    def exitTimes(self, ctx:IrregularParser.TimesContext):
        left = ctx.factor().code
        right = ctx.term().code
        ctx.code = left + " * " + right

    def exitDivision(self, ctx:IrregularParser.TimesContext):
        left = ctx.factor().code
        right = ctx.term().code
        ctx.code = left + " / " + right

    def exitFactorOnly(self, ctx:IrregularParser.FactorOnlyContext):
        ctx.code = ctx.factor().code

    def exitSum(self, ctx:IrregularParser.SumContext):
        left = ctx.term().code
        right = ctx.expr().code
        ctx.code = left + " + " + right

    def exitSubstraction(self, ctx:IrregularParser.SubstractionContext):
        left = ctx.term().code
        right = ctx.expr().code
        ctx.code = left + " - " + right

    def exitTermOnly(self, ctx:IrregularParser.TermOnlyContext):
        ctx.code = ctx.term().code

    def exitEvaluationLabel(self, ctx:IrregularParser.EvaluationLabelContext):
        function_name = ctx.evaluation().function_name().getText()
        params = ctx.evaluation().params_evaluation().getChildren()
        param_names = []
        for param in params:
            param_names.append(param.getText())
        param_with_comma = ', '.join(param_names)
        ctx.code = f"{function_name}({param_with_comma})"



if __name__ == '__main__':
    code_string = """
function sum a b c = a + b + c
function add_two x = x + 2
function add_three = (add_two x) + 1
function div_by_three x = x / 3
"""
    input_stream = InputStream(code_string)
    lexer = IrregularLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = IrregularParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    listener = SemanticListener()
    walker.walk(listener, tree) # Le indicamos al programa que camine sobre el arbol con el listener dado
    walkerCode = ParseTreeWalker()
    listenerCode = CodeGeneratorListener()
    walkerCode.walk(listenerCode, tree)
    print(tree.code)
