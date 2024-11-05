/*
int main(){
    return 0;
}
*/

grammar C;
INT: 'int';
MAIN: 'main';
RETURN: 'return';
PARENTHESIS_OPEN : '(';
PARENTHESIS_CLOSE : ')';
BRACE_OPEN: '{';
BRACE_CLOSE: '}';
WHITE_CHAR: [ ] -> skip;
TAB: '    ' | '\t';

prog: INT MAIN PARENTHESIS_OPEN PARENTHESIS_CLOSE BRACE_OPEN  '\n' TAB RETURN '0;' '\n' BRACE_CLOSE;

