grammar Grammar;

prog
    :   list* EOF
    ;

list
    : listitem+
    ;

listitem
    :   listprefix sentence
    |   rightanswer sentence
    ;

sentence
    :   (CHAR | WHITESPACE)+
    ;

listprefix
    :   LIST_PREFIX
    ;

rightanswer
    :   RIGHT_ANSWER_AFTER
        | RIGHT_ANSWER_BEFORE
    ;

listanswer
    :   rightanswer sentence
    ;

// ================================ TOKENS

NUMBER
    :   [0-9]+
    ;

CHAR
    :   [A-Za-z0-9\\]+
    ;   

LIST_PREFIX
    :   CHAR+  '\\'[.)]
    ;

WHITESPACE
    :   ' '
    ;

NEWLINE
    :   ('r'? 'n' | 'r')+ -> skip
    ;

RIGHT_ANSWER_AFTER
    :   CHAR+ WHITESPACE* [.)] WHITESPACE* '\\*'
    ;

RIGHT_ANSWER_BEFORE
    :  '\\*' WHITESPACE* CHAR+ WHITESPACE* [.)]
    ;
