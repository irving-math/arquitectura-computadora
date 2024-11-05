# Generated from antlr/Arithmetic.g4 by ANTLR 4.13.2
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
        4,1,8,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,32,8,2,1,3,1,3,1,3,1,3,1,3,3,3,39,8,3,1,3,0,0,4,0,2,4,
        6,0,0,41,0,8,1,0,0,0,2,20,1,0,0,0,4,31,1,0,0,0,6,38,1,0,0,0,8,9,
        3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,3,4,2,0,12,13,5,1,0,0,13,
        14,3,2,1,0,14,21,1,0,0,0,15,16,3,4,2,0,16,17,5,2,0,0,17,18,3,2,1,
        0,18,21,1,0,0,0,19,21,3,4,2,0,20,11,1,0,0,0,20,15,1,0,0,0,20,19,
        1,0,0,0,21,3,1,0,0,0,22,23,3,6,3,0,23,24,5,3,0,0,24,25,3,4,2,0,25,
        32,1,0,0,0,26,27,3,6,3,0,27,28,5,4,0,0,28,29,3,4,2,0,29,32,1,0,0,
        0,30,32,3,6,3,0,31,22,1,0,0,0,31,26,1,0,0,0,31,30,1,0,0,0,32,5,1,
        0,0,0,33,39,5,7,0,0,34,35,5,5,0,0,35,36,3,2,1,0,36,37,5,6,0,0,37,
        39,1,0,0,0,38,33,1,0,0,0,38,34,1,0,0,0,39,7,1,0,0,0,3,20,31,38
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FLOAT", "WHITE_CHAR" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "program", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    FLOAT=7
    WHITE_CHAR=8

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

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ArithmeticParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
            self.state = 9
            self.match(ArithmeticParser.EOF)
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
            return ArithmeticParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubstraction" ):
                listener.enterSubstraction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubstraction" ):
                listener.exitSubstraction(self)


    class SumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)


    class TermOnlyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermOnly" ):
                listener.enterTermOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermOnly" ):
                listener.exitTermOnly(self)



    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ArithmeticParser.SumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.term()
                self.state = 12
                self.match(ArithmeticParser.T__0)
                self.state = 13
                self.expr()
                pass

            elif la_ == 2:
                localctx = ArithmeticParser.SubstractionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.term()
                self.state = 16
                self.match(ArithmeticParser.T__1)
                self.state = 17
                self.expr()
                pass

            elif la_ == 3:
                localctx = ArithmeticParser.TermOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
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
            return ArithmeticParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TimesContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimes" ):
                listener.enterTimes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimes" ):
                listener.exitTimes(self)


    class DivisionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)

        def term(self):
            return self.getTypedRuleContext(ArithmeticParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivision" ):
                listener.enterDivision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivision" ):
                listener.exitDivision(self)


    class FactorOnlyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(ArithmeticParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorOnly" ):
                listener.enterFactorOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorOnly" ):
                listener.exitFactorOnly(self)



    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ArithmeticParser.TimesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.factor()
                self.state = 23
                self.match(ArithmeticParser.T__2)
                self.state = 24
                self.term()
                pass

            elif la_ == 2:
                localctx = ArithmeticParser.DivisionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.factor()
                self.state = 27
                self.match(ArithmeticParser.T__3)
                self.state = 28
                self.term()
                pass

            elif la_ == 3:
                localctx = ArithmeticParser.FactorOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
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
            return ArithmeticParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParenthesisContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)


    class FloatOnlyContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ArithmeticParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(ArithmeticParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatOnly" ):
                listener.enterFloatOnly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatOnly" ):
                listener.exitFloatOnly(self)



    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ArithmeticParser.FloatOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(ArithmeticParser.FLOAT)
                pass
            elif token in [5]:
                localctx = ArithmeticParser.ParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(ArithmeticParser.T__4)
                self.state = 35
                self.expr()
                self.state = 36
                self.match(ArithmeticParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





