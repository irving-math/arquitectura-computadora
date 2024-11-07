# Generated from antlr/Irregular.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,3,4,3,35,8,3,11,3,12,3,36,1,4,4,4,40,8,4,
        11,4,12,4,41,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,58,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,69,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,78,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,
        16,0,0,80,0,19,1,0,0,0,2,25,1,0,0,0,4,31,1,0,0,0,6,34,1,0,0,0,8,
        39,1,0,0,0,10,43,1,0,0,0,12,57,1,0,0,0,14,68,1,0,0,0,16,77,1,0,0,
        0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,5,8,0,0,26,
        27,3,4,2,0,27,28,3,6,3,0,28,29,5,10,0,0,29,30,3,12,6,0,30,3,1,0,
        0,0,31,32,5,9,0,0,32,5,1,0,0,0,33,35,5,9,0,0,34,33,1,0,0,0,35,36,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,7,1,0,0,0,38,40,5,9,0,0,39,
        38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,9,1,0,0,
        0,43,44,5,1,0,0,44,45,3,4,2,0,45,46,3,8,4,0,46,47,5,2,0,0,47,11,
        1,0,0,0,48,49,3,14,7,0,49,50,5,3,0,0,50,51,3,12,6,0,51,58,1,0,0,
        0,52,53,3,14,7,0,53,54,5,4,0,0,54,55,3,12,6,0,55,58,1,0,0,0,56,58,
        3,14,7,0,57,48,1,0,0,0,57,52,1,0,0,0,57,56,1,0,0,0,58,13,1,0,0,0,
        59,60,3,16,8,0,60,61,5,5,0,0,61,62,3,14,7,0,62,69,1,0,0,0,63,64,
        3,16,8,0,64,65,5,6,0,0,65,66,3,14,7,0,66,69,1,0,0,0,67,69,3,16,8,
        0,68,59,1,0,0,0,68,63,1,0,0,0,68,67,1,0,0,0,69,15,1,0,0,0,70,78,
        5,7,0,0,71,72,5,1,0,0,72,73,3,12,6,0,73,74,5,2,0,0,74,78,1,0,0,0,
        75,78,5,9,0,0,76,78,3,10,5,0,77,70,1,0,0,0,77,71,1,0,0,0,77,75,1,
        0,0,0,77,76,1,0,0,0,78,17,1,0,0,0,6,21,36,41,57,68,77
    ]

class IrregularParser ( Parser ):

    grammarFileName = "Irregular.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "<INVALID>", "'function'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FLOAT", "FUNCTION", 
                      "IDENTIFIER", "EQUAL", "WHITE_CHAR" ]

    RULE_program = 0
    RULE_function = 1
    RULE_function_name = 2
    RULE_params = 3
    RULE_params_evaluation = 4
    RULE_evaluation = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "program", "function", "function_name", "params", "params_evaluation", 
                   "evaluation", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    FLOAT=7
    FUNCTION=8
    IDENTIFIER=9
    EQUAL=10
    WHITE_CHAR=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IrregularParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IrregularParser.FunctionContext)
            else:
                return self.getTypedRuleContext(IrregularParser.FunctionContext,i)


        def getRuleIndex(self):
            return IrregularParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = IrregularParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.function()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 23
            self.match(IrregularParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(IrregularParser.FUNCTION, 0)

        def function_name(self):
            return self.getTypedRuleContext(IrregularParser.Function_nameContext,0)


        def params(self):
            return self.getTypedRuleContext(IrregularParser.ParamsContext,0)


        def EQUAL(self):
            return self.getToken(IrregularParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(IrregularParser.ExprContext,0)


        def getRuleIndex(self):
            return IrregularParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = IrregularParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(IrregularParser.FUNCTION)
            self.state = 26
            self.function_name()
            self.state = 27
            self.params()
            self.state = 28
            self.match(IrregularParser.EQUAL)
            self.state = 29
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IrregularParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return IrregularParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)




    def function_name(self):

        localctx = IrregularParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(IrregularParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(IrregularParser.IDENTIFIER)
            else:
                return self.getToken(IrregularParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return IrregularParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = IrregularParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.match(IrregularParser.IDENTIFIER)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_evaluationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(IrregularParser.IDENTIFIER)
            else:
                return self.getToken(IrregularParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return IrregularParser.RULE_params_evaluation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams_evaluation" ):
                listener.enterParams_evaluation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams_evaluation" ):
                listener.exitParams_evaluation(self)




    def params_evaluation(self):

        localctx = IrregularParser.Params_evaluationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_params_evaluation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.match(IrregularParser.IDENTIFIER)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_name(self):
            return self.getTypedRuleContext(IrregularParser.Function_nameContext,0)


        def params_evaluation(self):
            return self.getTypedRuleContext(IrregularParser.Params_evaluationContext,0)


        def getRuleIndex(self):
            return IrregularParser.RULE_evaluation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluation" ):
                listener.enterEvaluation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluation" ):
                listener.exitEvaluation(self)




    def evaluation(self):

        localctx = IrregularParser.EvaluationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_evaluation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(IrregularParser.T__0)
            self.state = 44
            self.function_name()
            self.state = 45
            self.params_evaluation()
            self.state = 46
            self.match(IrregularParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IrregularParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(IrregularParser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(IrregularParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstraction" ):
                listener.enterSubstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstraction" ):
                listener.exitSubstraction(self)


    class SumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(IrregularParser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(IrregularParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)


    class TermOnlyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(IrregularParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermOnly" ):
                listener.enterTermOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermOnly" ):
                listener.exitTermOnly(self)



    def expr(self):

        localctx = IrregularParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = IrregularParser.SumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.term()
                self.state = 49
                self.match(IrregularParser.T__2)
                self.state = 50
                self.expr()
                pass

            elif la_ == 2:
                localctx = IrregularParser.SubstractionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.term()
                self.state = 53
                self.match(IrregularParser.T__3)
                self.state = 54
                self.expr()
                pass

            elif la_ == 3:
                localctx = IrregularParser.TermOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IrregularParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TimesContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(IrregularParser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(IrregularParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimes" ):
                listener.enterTimes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimes" ):
                listener.exitTimes(self)


    class DivisionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(IrregularParser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(IrregularParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)


    class FactorOnlyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(IrregularParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorOnly" ):
                listener.enterFactorOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorOnly" ):
                listener.exitFactorOnly(self)



    def term(self):

        localctx = IrregularParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = IrregularParser.TimesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.factor()
                self.state = 60
                self.match(IrregularParser.T__4)
                self.state = 61
                self.term()
                pass

            elif la_ == 2:
                localctx = IrregularParser.DivisionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.factor()
                self.state = 64
                self.match(IrregularParser.T__5)
                self.state = 65
                self.term()
                pass

            elif la_ == 3:
                localctx = IrregularParser.FactorOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IrregularParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenthesisContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(IrregularParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)


    class IdentifierOnlyContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(IrregularParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierOnly" ):
                listener.enterIdentifierOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierOnly" ):
                listener.exitIdentifierOnly(self)


    class EvaluationLabelContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def evaluation(self):
            return self.getTypedRuleContext(IrregularParser.EvaluationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluationLabel" ):
                listener.enterEvaluationLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluationLabel" ):
                listener.exitEvaluationLabel(self)


    class FloatOnlyContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IrregularParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(IrregularParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatOnly" ):
                listener.enterFloatOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatOnly" ):
                listener.exitFloatOnly(self)



    def factor(self):

        localctx = IrregularParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = IrregularParser.FloatOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(IrregularParser.FLOAT)
                pass

            elif la_ == 2:
                localctx = IrregularParser.ParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(IrregularParser.T__0)
                self.state = 72
                self.expr()
                self.state = 73
                self.match(IrregularParser.T__1)
                pass

            elif la_ == 3:
                localctx = IrregularParser.IdentifierOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(IrregularParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = IrregularParser.EvaluationLabelContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.evaluation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





