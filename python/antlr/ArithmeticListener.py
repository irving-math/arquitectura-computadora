# Generated from antlr/Arithmetic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#Sum.
    def enterSum(self, ctx:ArithmeticParser.SumContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Sum.
    def exitSum(self, ctx:ArithmeticParser.SumContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Substraction.
    def enterSubstraction(self, ctx:ArithmeticParser.SubstractionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Substraction.
    def exitSubstraction(self, ctx:ArithmeticParser.SubstractionContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#TermOnly.
    def enterTermOnly(self, ctx:ArithmeticParser.TermOnlyContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#TermOnly.
    def exitTermOnly(self, ctx:ArithmeticParser.TermOnlyContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Times.
    def enterTimes(self, ctx:ArithmeticParser.TimesContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Times.
    def exitTimes(self, ctx:ArithmeticParser.TimesContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Division.
    def enterDivision(self, ctx:ArithmeticParser.DivisionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Division.
    def exitDivision(self, ctx:ArithmeticParser.DivisionContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#FactorOnly.
    def enterFactorOnly(self, ctx:ArithmeticParser.FactorOnlyContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#FactorOnly.
    def exitFactorOnly(self, ctx:ArithmeticParser.FactorOnlyContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#FloatOnly.
    def enterFloatOnly(self, ctx:ArithmeticParser.FloatOnlyContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#FloatOnly.
    def exitFloatOnly(self, ctx:ArithmeticParser.FloatOnlyContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#Parenthesis.
    def enterParenthesis(self, ctx:ArithmeticParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#Parenthesis.
    def exitParenthesis(self, ctx:ArithmeticParser.ParenthesisContext):
        pass



del ArithmeticParser