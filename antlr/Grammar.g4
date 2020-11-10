grammar Grammar;

// options 
// {
// output=AST;
// backtrack=true;
// memoize=true;
// }

prog
    :   answeritem* EOF
    ;

answeritem
    :   answerprefix content answerfeedback
    |   answerprefix content 
    ;
content
    :   ALL_CHARACTER+
    ;
answerprefix
    :   RIGHT_ANSWER_AFTER
    |   RIGHT_ANSWER_BEFORE
    ;

answerfeedback
    :   FEEDBACKMARKER content
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

fragment WHITESPACE
    :   ' '
    ;

fragment CHAR:
    ~('')
    ;

fragment NUMBER
    :   DIGIT+ (DIGIT+)?
    ;

fragment ATSYMBOL
    :   '@'
    ;

fragment COLON
    :   ':'
    ;

fragment NEWLINE
    :   ('\n')
    ;

fragment ANSWER_MARKER
    : BACKSLASH ASTERISK
    ;


FEEDBACKMARKER
    // :   ATSYMBOL WHITESPACE* ('Feedback'|'feedback') WHITESPACE* COLON
    :   NEWLINE+ WHITESPACE* ATSYMBOL WHITESPACE*
    ;

ALL_CHARACTER
    : CHAR
    ;
    
ALPHANUMERIC
    :   (LOWERCASE | UPPERCASE | NUMBER)
    ;


RIGHT_ANSWER_AFTER
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* ANSWER_MARKER WHITESPACE*
    ;

RIGHT_ANSWER_BEFORE
    :   NEWLINE WHITESPACE* ANSWER_MARKER WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;

LIST_ITEM
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;
