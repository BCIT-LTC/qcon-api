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

fragment DIGIT
    :   [0-9]
    ;

fragment LOWERCASE
    : [a-z]
    ;

fragment UPPERCASE
    : [A-Z]
    ;

fragment BACKSLASH
    : '\\'
    ;

fragment DOT
    : '.'
    ;

fragment CLOSING_PARENTHESIS
    : ')'
    ;

fragment ASTERISK
    : '*'
    ;

ANSWER_MARKER
    : BACKSLASH ASTERISK
    ;

DECIMAL
    : DIGIT+ ([.,] DIGIT+)?
    ;

NUMBER
    :   DIGIT+ (DIGIT+)?
    ;

CHAR
    :   (LOWERCASE | UPPERCASE | NUMBER | DECIMAL)+
    ;   

LIST_PREFIX
    :   CHAR+  '\\' (DOT | CLOSING_PARENTHESIS)
    ;

WHITESPACE
    :   ' '
    ;

NEWLINE
    :   ('r'? 'n' | 'r')+ -> skip
    ;

RIGHT_ANSWER_AFTER
    :   CHAR+ BACKSLASH WHITESPACE* (DOT | CLOSING_PARENTHESIS) WHITESPACE* ANSWER_MARKER
    ;

RIGHT_ANSWER_BEFORE
    :  ANSWER_MARKER WHITESPACE* CHAR+ WHITESPACE* BACKSLASH (DOT | CLOSING_PARENTHESIS)
    ;
