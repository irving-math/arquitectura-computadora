/*
S -> aSa
S -> bSb
S -> e
S -> a
S -> b
*/

grammar Palindrome;
A: 'a';
B: 'b';
palindrome: A palindrome A | B palindrome B | A | B | ;
WHITE_CHAR: [\n\r\t] -> skip;