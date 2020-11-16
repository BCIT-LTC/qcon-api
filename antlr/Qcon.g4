grammar Qcon;

// options 
// {
// output=AST;
// backtrack=true;
// memoize=true;
// }

// @parser::members{
// public class Question {

    
//     }
// }

qcon
    :   question* EOF
    ;

question
    :   questionbody answerlist feedback?
    ;
    

questionbody
    :   questionprefix content feedback?
    |   questiontype? title? point? questionprefix content feedback?
    |   questiontype? point? title? questionprefix content feedback?
    |   title? questiontype? point? questionprefix content feedback?
    |   title? point? questiontype? questionprefix content feedback?
    |   point? questiontype? title? questionprefix content feedback?
    |   point? title? questiontype? questionprefix content feedback?
    ;

questiontype
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

// list
//     :   (listitem)+ (list+)?
//     ;

answerlist
    :   answeritem+ (answerlist+)?
    // :   (listitem|answeritem) answerlist
    // |   listitem
    // |   answerlist
    ;

answeritem
    :   listitem
    |   listansweritem
    ;

listitem
    // :   listprefix content feedback?
    :   listprefix content feedback
    |   listprefix content
    ;

listansweritem
    // :   answerprefix content feedback?
    :   answerprefix content feedback
    |   answerprefix content
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
    :   ('\r'? '\n' | '\r')
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
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (UPPERCASE | LOWERCASE)+ WHITESPACE*
    ;

TITLE
    :   NEWLINE+ WHITESPACE* T I T L E S? WHITESPACE* COLON WHITESPACE* ~('\n')+ WHITESPACE*
    ;

POINT
    :   NEWLINE+ WHITESPACE* P O I N T S? WHITESPACE* COLON WHITESPACE* DECIMAL WHITESPACE*
    ;

QUESTION_PREFIX
    :   NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
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


