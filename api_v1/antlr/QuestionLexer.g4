lexer grammar QuestionLexer;

tokens {START_QUESTION_HEADER, START_QUESTION, END_ANSWERS, FEEDBACK_MARKER, MEDIA, HYPERLINK, ALL_CHARACTER, ESCAPED_OPEN_BRACKET, ESCAPED_CLOSE_BRACKET}

fragment QUESTION_HEADER_MARKER
    :   '##########_QUESTION_HEADER_##########'
    ;

fragment START_QUESTION_MARKER
    :   '##########_START_QUESTION_##########'
    ;

fragment END_ANSWERS_MARKER
    :   '##########_END_ANSWERS_##########'
    ;

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

// --------------------- DEFAULT MODE ---------------------
DEFAULT_START_HEADER
    :   NEWLINE+ QUESTION_HEADER_MARKER                 -> type(START_QUESTION_HEADER), mode(HEADER_CONTENT)
    ;

DEFAULT_START_QUESTION
    :   NEWLINE+ START_QUESTION_MARKER NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* -> type(START_QUESTION), mode(QUESTION_CONTENT)
    ;

SECTION_TITLE
    :   NEWLINE+ '##########_SECTION_##########'
    ;

DEFAULT_ALL_CHARACTER
    :   CHAR                                            -> type(ALL_CHARACTER)
    ;


// --------------------- Everything AFTER QUESTION_HEADER marker ---------------------
mode HEADER_CONTENT;

HEADER_START_QUESTION
    :   NEWLINE+ START_QUESTION_MARKER NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* -> type(START_QUESTION), mode(QUESTION_CONTENT)
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
    :   NEWLINE+ WHITESPACE* T Y P E S? WHITESPACE* COLON WHITESPACE* ~('\n')+
    ;


// --------------------- Everything AFTER START_QUESTION marker ---------------------
mode QUESTION_CONTENT;

CONTENT_START_HEADER
    :   NEWLINE+ QUESTION_HEADER_MARKER                             -> type(START_QUESTION_HEADER), mode(HEADER_CONTENT)
    ;

// If a question after question
CONTENT_START_QUESTION
    :   NEWLINE+ START_QUESTION_MARKER NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* -> type(START_QUESTION)
    ;

START_ANSWER
    :   NEWLINE+ '##########_START_ANSWER_##########'               -> mode(ANSWER_CONTENT)
    ;

QUESTION_END_ANSWERS
    :   NEWLINE+ END_ANSWERS_MARKER NEWLINE+ WHITESPACE* A N S W E R S? WHITESPACE* COLON WHITESPACE* -> type(END_ANSWERS), mode(ANSWER_KEY)
    ;

QUESTION_FEEDBACK_MARKER
    :   NEWLINE+ WHITESPACE* '@' WHITESPACE*                        -> type(FEEDBACK_MARKER)
    ;
    
QUESTION_MEDIA
    :   '!' OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'      -> type(MEDIA)
    ;

QUESTION_HYPERLINK
    :   OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'          -> type(HYPERLINK)
    ;

QUESTION_ALL_CHARACTER
    :   CHAR                                                        -> type(ALL_CHARACTER)
    ;

QUESTION_ESCAPED_OPEN_BRACKET
    :   BACKSLASH OPEN_BRACKET                                      -> type(ESCAPED_OPEN_BRACKET)
    ;

QUESTION_ESCAPED_CLOSE_BRACKET
    :   BACKSLASH CLOSE_BRACKET                                     -> type(ESCAPED_CLOSE_BRACKET)
    ;

    
// --------------------- Everything AFTER START_ANSWER marker ---------------------
mode ANSWER_CONTENT;

ANSWER_START_HEADER
    :   NEWLINE+ QUESTION_HEADER_MARKER                             -> type(START_QUESTION_HEADER), mode(HEADER_CONTENT)
    ;

ANSWER_START_QUESTION
    :   NEWLINE+ START_QUESTION_MARKER NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* -> type(START_QUESTION), mode(QUESTION_CONTENT)
    ;

ANSWER_END_ANSWERS
    :   NEWLINE+ END_ANSWERS_MARKER NEWLINE+ WHITESPACE* A N S W E R S? WHITESPACE* COLON WHITESPACE* -> type(END_ANSWERS), mode(ANSWER_KEY)
    ;

RIGHT_ANSWER
    :   NEWLINE+ WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE* ANSWER_MARKER WHITESPACE*
    ;

LIST_PREFIX
    :   NEWLINE+ WHITESPACE* ALPHANUMERIC ALPHANUMERIC? WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;

ANSWER_FEEDBACK_MARKER
    :   NEWLINE+ WHITESPACE* '@' WHITESPACE*                        -> type(FEEDBACK_MARKER)
    ;
    
ANSWER_MEDIA
    :   '!' OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'      -> type(MEDIA)
    ;

ANSWER_HYPERLINK
    :   OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'          -> type(HYPERLINK)
    ;

ANSWER_ALL_CHARACTER
    :   CHAR                                                        -> type(ALL_CHARACTER)
    ;

ANSWER_ESCAPED_OPEN_BRACKET
    :   BACKSLASH OPEN_BRACKET                                      -> type(ESCAPED_OPEN_BRACKET)
    ;

ANSWER_ESCAPED_CLOSE_BRACKET
    :   BACKSLASH CLOSE_BRACKET                                     -> type(ESCAPED_CLOSE_BRACKET)
    ;

// --------------------- Everything AFTER END_ANSWERS marker ---------------------
mode ANSWER_KEY;

QUESTION_PREFIX
    :   NEWLINE+ WHITESPACE* NUMBER WHITESPACE* BACKSLASH? (DOT | CLOSING_PARENTHESIS) WHITESPACE*
    ;

KEY_FEEDBACK_MARKER
    :   NEWLINE+ WHITESPACE* '@' WHITESPACE*                        -> type(FEEDBACK_MARKER)
    ;
    
KEY_MEDIA
    :   '!' OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'      -> type(MEDIA)
    ;

KEY_HYPERLINK
    :   OPEN_BRACKET ~(']')* CLOSE_BRACKET '(' ~(')')* ')'          -> type(HYPERLINK)
    ;

KEY_ALL_CHARACTER
    :   CHAR                                                        -> type(ALL_CHARACTER)
    ;

KEY_ESCAPED_OPEN_BRACKET
    :   BACKSLASH OPEN_BRACKET                                      -> type(ESCAPED_OPEN_BRACKET)
    ;

KEY_ESCAPED_CLOSE_BRACKET
    :   BACKSLASH CLOSE_BRACKET                                     -> type(ESCAPED_CLOSE_BRACKET)
    ;

