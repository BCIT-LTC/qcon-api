grammar Grammar;

// options 
// {
// output=AST;
// backtrack=true;
// memoize=true;
// }

prog
    :   question* EOF
    ;

question
    :   questionbody answerlist feedback?
    ;

questionbody
    :   questionprefix content feedback?
    |   type? title? point? questionprefix content feedback?
    |   type? point? title? questionprefix content feedback?
    |   title? type? point? questionprefix content feedback?
    |   title? point? type? questionprefix content feedback?
    |   point? type? title? questionprefix content feedback?
    |   point? title? type? questionprefix content feedback?
    ;

type
    :   TYPE
    ;

title
    :   TITLE
    ;

point
    :   POINT
    ;

content
    :   ALL_CHARACTER+
    ;

list
    :   (listitem)+ (list+)?
    ;

answerlist
    :   (listitem|answeritem)+ (answerlist+)?
    ;

listitem
    :   listprefix content feedback?
    ;

answeritem
    :   answerprefix content feedback?
    ;


questionprefix
    :   QUESTION_PREFIX
    ;

listprefix
    :   LIST_PREFIX
    ;

answerprefix
    :   RIGHT_ANSWER_AFTER
    |   RIGHT_ANSWER_BEFORE
    ;

feedback
    :   FEEDBACKMARKER content
    ;

// ================================ TOKENS

fragment DIGIT
    :   [0-9]
    ;

fragment LOWERCASE
    :   [a-z]
    ;

fragment UPPERCASE
    :   [A-Z]
    ;

fragment BACKSLASH
    :   '\\'
    ;

fragment DOT
    :   '.'
    ;

fragment CLOSING_PARENTHESIS
    :   ')'
    ;

fragment ASTERISK
    :   '*'
    ;

fragment WHITESPACE
    :   ' '
    | '\t'
    ;

fragment CHAR
    // ☢ BIOHAZARD SYMBOL (HEX)
    :   ~([\u{2622}])
    ;

fragment NUMBER
    :   DIGIT+ (DIGIT+)?
    ;

fragment DECIMAL
    :    DIGIT+ DOT? (DIGIT+)?
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
    :   BACKSLASH ASTERISK
    ;

fragment E
    :   'E' | 'e'
    ;
fragment I
    :   'I' | 'i'
    ;

fragment L
    :   'L' | 'l'
    ;

fragment N
    :   'N' | 'n'
    ;

fragment O
    :   'O' | 'o'
    ;

fragment P
    :   'P' | 'p'
    ;

fragment S
    :   'S' | 's'
    ;

fragment T
    :   'T' | 't'
    ;

fragment Y
    :   'Y' | 'y'
    ;  

fragment ALPHANUMERIC
    :   (LOWERCASE | UPPERCASE | NUMBER)
    ;

FEEDBACKMARKER
    // :   ATSYMBOL WHITESPACE* ('Feedback'|'feedback') WHITESPACE* COLON
    :   NEWLINE+ WHITESPACE* ATSYMBOL WHITESPACE*
    ;
    
    
TYPE
    :   NEWLINE WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (UPPERCASE | LOWERCASE)+ WHITESPACE*
    ;

TITLE
    :   NEWLINE WHITESPACE* T I T L E S? WHITESPACE* COLON WHITESPACE* ~('\n')+ WHITESPACE*
    ;

POINT
    :   NEWLINE WHITESPACE* P O I N T S? WHITESPACE* COLON WHITESPACE* DECIMAL WHITESPACE*
    ;

QUESTION_PREFIX
:   NEWLINE WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
;

LIST_PREFIX
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;
ALL_CHARACTER
    :   CHAR
    ;

RIGHT_ANSWER_AFTER
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* ANSWER_MARKER WHITESPACE*
    ;

RIGHT_ANSWER_BEFORE
    :   NEWLINE WHITESPACE* ANSWER_MARKER WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;


