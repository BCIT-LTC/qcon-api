lexer grammar QuestionLexer;

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

fragment C
    :   'C' | 'c'
    ;

fragment D
    :   'D' | 'd'
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

TITLE
    :   NEWLINE+ WHITESPACE* T I T L E S? WHITESPACE* COLON WHITESPACE* ~('\n')+ WHITESPACE*
    ;

POINTS
    :   NEWLINE+ WHITESPACE* P O I N T S? WHITESPACE* COLON WHITESPACE* DECIMAL WHITESPACE*
    ;

TYPE_MC
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* M C WHITESPACE*
    ;

TYPE_TF
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* T F WHITESPACE*
    ;

TYPE_MS
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (M S | M R) WHITESPACE*
    ;

TYPE_MT
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* M T WHITESPACE*
    ;

TYPE_ORD
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* O R D WHITESPACE*
    ;

TYPE_FIB
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (F I B | F M B) WHITESPACE*
    ;

TYPE_WR
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (W R | E) WHITESPACE*
    ;

TYPE_OTHER
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* (CHAR)+ WHITESPACE*
    ;

QUESTION_PREFIX
    :   NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* -> pushMode(QUESTION_CONTENT)
    ;


// --------------------- Everything AFTER question number ---------------------
mode QUESTION_CONTENT;

FEEDBACK_MARKER
    :   NEWLINE+ BLOCKQUOTE? WHITESPACE* ATSYMBOL WHITESPACE*
    ;
    
LIST_PREFIX
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;

MEDIA
    :   '!' OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'
    ;

HYPERLINK
    :   OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'
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

ESCAPED_OPEN_BRACKET
    :   BACKSLASH OPEN_BRACKET
    ;

ESCAPED_CLOSE_BRACKET
    :   BACKSLASH CLOSE_BRACKET
    ;