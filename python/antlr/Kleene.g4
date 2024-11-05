grammar Kleene;
LETTER_A: 'a';
WHITE_CHAR: [\n\r\t] -> skip;

s: s LETTER_A |;

