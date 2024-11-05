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
        4,1,8,36,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,3,0,16,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,
        2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,2,0,0,3,0,2,4,0,0,37,0,15,1,0,0,0,
        2,26,1,0,0,0,4,33,1,0,0,0,6,7,3,2,1,0,7,8,5,1,0,0,8,9,3,0,0,0,9,
        16,1,0,0,0,10,11,3,2,1,0,11,12,5,2,0,0,12,13,3,0,0,0,13,16,1,0,0,
        0,14,16,3,2,1,0,15,6,1,0,0,0,15,10,1,0,0,0,15,14,1,0,0,0,16,1,1,
        0,0,0,17,18,3,4,2,0,18,19,5,3,0,0,19,20,3,2,1,0,20,27,1,0,0,0,21,
        22,3,4,2,0,22,23,5,4,0,0,23,24,3,2,1,0,24,27,1,0,0,0,25,27,3,4,2,
        0,26,17,1,0,0,0,26,21,1,0,0,0,26,25,1,0,0,0,27,3,1,0,0,0,28,34,5,
        7,0,0,29,30,5,5,0,0,30,31,3,0,0,0,31,32,5,6,0,0,32,34,1,0,0,0,33,
        28,1,0,0,0,33,29,1,0,0,0,34,5,1,0,0,0,3,15,26,33
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "FLOAT", "WHITE_CHAR" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expr", "term", "factor" ]

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
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ArithmeticParser.SumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.term()
                self.state = 7
                self.match(ArithmeticParser.T__0)
                self.state = 8
                self.expr()
                pass

            elif la_ == 2:
                localctx = ArithmeticParser.SubstractionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.term()
                self.state = 11
                self.match(ArithmeticParser.T__1)
                self.state = 12
                self.expr()
                pass

            elif la_ == 3:
                localctx = ArithmeticParser.TermOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
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
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = ArithmeticParser.TimesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.factor()
                self.state = 18
                self.match(ArithmeticParser.T__2)
                self.state = 19
                self.term()
                pass

            elif la_ == 2:
                localctx = ArithmeticParser.DivisionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.factor()
                self.state = 22
                self.match(ArithmeticParser.T__3)
                self.state = 23
                self.term()
                pass

            elif la_ == 3:
                localctx = ArithmeticParser.FactorOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
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
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = ArithmeticParser.FloatOnlyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(ArithmeticParser.FLOAT)
                pass
            elif token in [5]:
                localctx = ArithmeticParser.ParenthesisContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(ArithmeticParser.T__4)
                self.state = 30
                self.expr()
                self.state = 31
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





