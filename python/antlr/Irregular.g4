grammar Irregular;

FLOAT: [0-9]+ | [0-9]+'.'[0-9]+;
FUNCTION: 'function';
IDENTIFIER: [a-z]+ ('_'|[a-z]+)*;
EQUAL: '=';


program: function+ EOF;

function: FUNCTION function_name params EQUAL expr;

function_name: IDENTIFIER;

params: IDENTIFIER +;
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
    | IDENTIFIER # IdentifierOnly
    ;

WHITE_CHAR : [ \n] -> skip;
