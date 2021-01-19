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

fragment U
    :   'U' | 'u'
    ;

fragment W
    :   'W' | 'w'
    ;

fragment Y
    :   'Y' | 'y'
    ;  

fragment Z
    :   'Z' | 'z'
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

TITLE
    :   NEWLINE+ WHITESPACE* T I T L E S? WHITESPACE* COLON WHITESPACE* ~('\n')+ WHITESPACE*
    ;

POINTS
    :   NEWLINE+ WHITESPACE* P O I N T S? WHITESPACE* COLON WHITESPACE* DECIMAL WHITESPACE*
    ;

RANDOMIZE_TRUE
    :   NEWLINE+ WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE* COLON WHITESPACE* (T R U E | Y E S) WHITESPACE*
    ;

RANDOMIZE_FALSE
    :   NEWLINE+ WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE* COLON WHITESPACE* (F A L S E | N O) WHITESPACE*
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

START_ANSWER
    :   '##########_START_ANSWER_##########' -> pushMode(ANSWER_CONTENT)
    ;

FEEDBACK_MARKER
    :   NEWLINE+ WHITESPACE* '@' WHITESPACE*
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

ESCAPED_OPEN_BRACKET
    :   BACKSLASH OPEN_BRACKET
    ;

ESCAPED_CLOSE_BRACKET
    :   BACKSLASH CLOSE_BRACKET
    ;
    
// --------------------- Everything AFTER start answer marker ---------------------
mode ANSWER_CONTENT;

END_ANSWER
    :   '##########_END_ANSWER_##########' NEWLINE*
    ;

RIGHT_ANSWER
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* ANSWER_MARKER WHITESPACE*
    ;

ANSWER_FEEDBACK_MARKER
    :   FEEDBACK_MARKER             -> type(FEEDBACK_MARKER)
    ;

LIST_PREFIX
    :   NEWLINE WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;

ANSWER_MEDIA
    :   MEDIA                       -> type(MEDIA)
    ;

ANSWER_HYPERLINK
    :   HYPERLINK                   -> type(HYPERLINK)
    ;

ALL_CHAR
    :   ALL_CHARACTER               -> type(ALL_CHARACTER)
    ;

FIB_OPEN_BRACKET
    :   ESCAPED_OPEN_BRACKET        -> type(ESCAPED_OPEN_BRACKET)
    ;

FIB_CLOSE_BRACKET
    :   ESCAPED_CLOSE_BRACKET       -> type(ESCAPED_CLOSE_BRACKET)
    ;