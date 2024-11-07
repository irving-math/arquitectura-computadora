# Generated from antlr/Irregular.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IrregularParser import IrregularParser
else:
    from IrregularParser import IrregularParser

# This class defines a complete listener for a parse tree produced by IrregularParser.
class IrregularListener(ParseTreeListener):

    # Enter a parse tree produced by IrregularParser#program.
    def enterProgram(self, ctx:IrregularParser.ProgramContext):
        pass

    # Exit a parse tree produced by IrregularParser#program.
    def exitProgram(self, ctx:IrregularParser.ProgramContext):
        pass


    # Enter a parse tree produced by IrregularParser#function.
    def enterFunction(self, ctx:IrregularParser.FunctionContext):
        pass

    # Exit a parse tree produced by IrregularParser#function.
    def exitFunction(self, ctx:IrregularParser.FunctionContext):
        pass


    # Enter a parse tree produced by IrregularParser#function_name.
    def enterFunction_name(self, ctx:IrregularParser.Function_nameContext):
        pass

    # Exit a parse tree produced by IrregularParser#function_name.
    def exitFunction_name(self, ctx:IrregularParser.Function_nameContext):
        pass


    # Enter a parse tree produced by IrregularParser#params.
    def enterParams(self, ctx:IrregularParser.ParamsContext):
        pass

    # Exit a parse tree produced by IrregularParser#params.
    def exitParams(self, ctx:IrregularParser.ParamsContext):
        pass


    # Enter a parse tree produced by IrregularParser#params_evaluation.
    def enterParams_evaluation(self, ctx:IrregularParser.Params_evaluationContext):
        pass

    # Exit a parse tree produced by IrregularParser#params_evaluation.
    def exitParams_evaluation(self, ctx:IrregularParser.Params_evaluationContext):
        pass


    # Enter a parse tree produced by IrregularParser#evaluation.
    def enterEvaluation(self, ctx:IrregularParser.EvaluationContext):
        pass

    # Exit a parse tree produced by IrregularParser#evaluation.
    def exitEvaluation(self, ctx:IrregularParser.EvaluationContext):
        pass


    # Enter a parse tree produced by IrregularParser#Sum.
    def enterSum(self, ctx:IrregularParser.SumContext):
        pass

    # Exit a parse tree produced by IrregularParser#Sum.
    def exitSum(self, ctx:IrregularParser.SumContext):
        pass


    # Enter a parse tree produced by IrregularParser#Substraction.
    def enterSubstraction(self, ctx:IrregularParser.SubstractionContext):
        pass

    # Exit a parse tree produced by IrregularParser#Substraction.
    def exitSubstraction(self, ctx:IrregularParser.SubstractionContext):
        pass


    # Enter a parse tree produced by IrregularParser#TermOnly.
    def enterTermOnly(self, ctx:IrregularParser.TermOnlyContext):
        pass

    # Exit a parse tree produced by IrregularParser#TermOnly.
    def exitTermOnly(self, ctx:IrregularParser.TermOnlyContext):
        pass


    # Enter a parse tree produced by IrregularParser#Times.
    def enterTimes(self, ctx:IrregularParser.TimesContext):
        pass

    # Exit a parse tree produced by IrregularParser#Times.
    def exitTimes(self, ctx:IrregularParser.TimesContext):
        pass


    # Enter a parse tree produced by IrregularParser#Division.
    def enterDivision(self, ctx:IrregularParser.DivisionContext):
        pass

    # Exit a parse tree produced by IrregularParser#Division.
    def exitDivision(self, ctx:IrregularParser.DivisionContext):
        pass


    # Enter a parse tree produced by IrregularParser#FactorOnly.
    def enterFactorOnly(self, ctx:IrregularParser.FactorOnlyContext):
        pass

    # Exit a parse tree produced by IrregularParser#FactorOnly.
    def exitFactorOnly(self, ctx:IrregularParser.FactorOnlyContext):
        pass


    # Enter a parse tree produced by IrregularParser#FloatOnly.
    def enterFloatOnly(self, ctx:IrregularParser.FloatOnlyContext):
        pass

    # Exit a parse tree produced by IrregularParser#FloatOnly.
    def exitFloatOnly(self, ctx:IrregularParser.FloatOnlyContext):
        pass


    # Enter a parse tree produced by IrregularParser#Parenthesis.
    def enterParenthesis(self, ctx:IrregularParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by IrregularParser#Parenthesis.
    def exitParenthesis(self, ctx:IrregularParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by IrregularParser#IdentifierOnly.
    def enterIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        pass

    # Exit a parse tree produced by IrregularParser#IdentifierOnly.
    def exitIdentifierOnly(self, ctx:IrregularParser.IdentifierOnlyContext):
        pass


    # Enter a parse tree produced by IrregularParser#EvaluationLabel.
    def enterEvaluationLabel(self, ctx:IrregularParser.EvaluationLabelContext):
        pass

    # Exit a parse tree produced by IrregularParser#EvaluationLabel.
    def exitEvaluationLabel(self, ctx:IrregularParser.EvaluationLabelContext):
        pass



del IrregularParser