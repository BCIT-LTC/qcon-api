grammar Qcon;



qcon
    :   question* endanswers? EOF
    ;

question
    : fibquestionbody           # FibQuestion
    | questionbody answerlist   # QuestionWithAnswers
    | questionbody              # QuestionWithoutAnswers
    ;

endanswers
    :   endanswerstart endanswerlistitem+
    ;

questionbody
    :   questionprefix content+ feedback?
    |   questiontype? title? point? questionprefix content feedback?
    |   questiontype? point? title? questionprefix content feedback?
    |   title? questiontype? point? questionprefix content feedback?
    |   title? point? questiontype? questionprefix content feedback?
    |   point? questiontype? title? questionprefix content feedback?
    |   point? title? questiontype? questionprefix content feedback?
    ;

fibquestionbody
    :   questionprefix fibcontent+ feedback?
    |   fibtype? title? point? questionprefix fibcontent+ feedback?
    |   fibtype? point? title? questionprefix fibcontent+ feedback?
    |   title? fibtype? point? questionprefix fibcontent+ feedback?
    |   title? point? fibtype? questionprefix fibcontent+ feedback?
    |   point? fibtype? title? questionprefix fibcontent+ feedback?
    |   point? title? fibtype? questionprefix fibcontent+ feedback?
    ;

fibcontent
    :   fibanswer 
    |   content
    ;

fibtype
    :   FIB_TYPE
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

fibanswer
    :   FIB_OPEN_BRACKET ALL_CHARACTER+ FIB_CLOSE_BRACKET
    ;

content
    : HYPERLINK
    | ALL_CHARACTER+
    ;

// list
//     :   (listitem)+ (list+)?
//     ;

answerlist
    :   // answeritem+ (answerlist+)?
    listitem+                         # NoAnswerExist
    | (listansweritem | listitem)+    # AnswerExist
    ;

// answeritem
//     :   listitem
//     |   listansweritem
//     ;

listitem
    :   listprefix content feedback?
    ;

listansweritem
    :   answerprefix content feedback?
    ;

endanswerlistitem
    :   questionprefix content feedback?
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

endanswerstart
    :   END_ANSWERS
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
    :   .
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

fragment A
    :   'A' | 'a'
    ;

fragment B
    :   'B' | 'b'
    ;

fragment E
    :   'E' | 'e'
    ;

fragment F
    :   'F' | 'f'
    ;

fragment I
    :   'I' | 'i'
    ;

fragment L
    :   'L' | 'l'
    ;

fragment M
    :   'M' | 'm'
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

fragment R
    :   'R' | 'r'
    ;

fragment S
    :   'S' | 's'
    ;

fragment T
    :   'T' | 't'
    ;

fragment W
    :   'W' | 'w'
    ;

fragment Y
    :   'Y' | 'y'
    ;  

fragment OPEN_BRACKET
    :   '['
    ;

 fragment CLOSE_BRACKET
    :   ']'
    ;

fragment ALPHANUMERIC
    :   (LOWERCASE | UPPERCASE | NUMBER)
    ;

fragment BLOCKQUOTE
    :   '>'
    ;

FEEDBACKMARKER
    // :   ATSYMBOL WHITESPACE* ('Feedback'|'feedback') WHITESPACE* COLON
    :   NEWLINE+ BLOCKQUOTE? WHITESPACE* ATSYMBOL WHITESPACE*
    ;
    
END_ANSWERS
    :   NEWLINE+ WHITESPACE* A N S W E R S? WHITESPACE* COLON WHITESPACE*
    ;

TYPE
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (UPPERCASE | LOWERCASE)+ WHITESPACE*
    ;

FIB_TYPE
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (F I B | F M B) WHITESPACE*
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

HYPERLINK: WHITESPACE* '!' OPEN_BRACKET CHAR* CLOSE_BRACKET '(' CHAR* ')' ;

FIB_OPEN_BRACKET
    :   WHITESPACE* BACKSLASH? OPEN_BRACKET WHITESPACE*
    ;

FIB_CLOSE_BRACKET
    :   WHITESPACE* BACKSLASH? CLOSE_BRACKET WHITESPACE*
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

