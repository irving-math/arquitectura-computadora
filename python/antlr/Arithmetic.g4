grammar Arithmetic;

FLOAT: [0-9]+;

program: expr EOF;

expr: term '+' expr # Sum
    | term '-' expr # Substraction
    | term # TermOnly
    ;
term: factor '*' term # Times
    | factor '/' term # Division
    | factor # FactorOnly
    ;
factor: FLOAT # FloatOnly
    | '(' expr ')' # Parenthesis
    ;

WHITE_CHAR : [ ] -> skip;
