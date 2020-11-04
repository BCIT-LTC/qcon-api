grammar Grammar;

prog
    :   listitem* EOF
    ;

listitem
    :   listprefix sentence
    ;

sentence
    :   sentence WORD 
    |   WORD
    ;

listprefix
    :   LIST_PREFIX
    ;

// ================================ TOKENS

NUMBER
    :   [0-9]+
    ;

WORD
    :   [A-Za-z\\]+
    ;   

LIST_PREFIX
    :   [A-Za-z0-9]+ '\\.'
    |   [A-Za-z0-9]+ ')'
    ;

SPACE
    :   ' ' -> skip
    ;

// WS
//     :   [ \t\r\n]+ -> skip
//     ;
