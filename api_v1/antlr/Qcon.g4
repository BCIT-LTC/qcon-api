grammar Qcon;

qcon
    :   question* end_answers? EOF
    ;

question
    :   question_header question_body answerlist   # QuestionWithAnswers
    |   question_header question_body              # QuestionWithoutAnswers
    ;

end_answers
    :   end_answers_start end_answers_list_item+
    ;

question_body
    :   question_prefix content+ feedback?      # RegularQuestion
    |   question_prefix fib_content+ feedback?  # FibQuestion
    ;

fib_content
    :   fib_answer 
    |   content
    ;

question_header
    :   question_type? title? point?
    |   title? question_type? point?
    |   point? question_type? title?
    ;

question_type
    :   TYPE_MC         # TypeMc
    |   TYPE_TF         # TypeTf
    |   TYPE_MS         # TypeMs
    |   TYPE_MT         # TypeMt
    |   TYPE_ORD        # TypeOrd
    |   TYPE_FIB        # TypeFib
    |   TYPE_WR         # TypeWr
    |   TYPE_OTHER      # TypeOther
    ;

title
    :   TITLE
    ;

point
    :   POINT
    ;

fib_answer
    :   FIB_OPEN_BRACKET ALL_CHARACTER+ FIB_CLOSE_BRACKET
    ;

content
    :   HYPERLINK
    |   ALL_CHARACTER+
    ;


answerlist
    :   list_item+                          # NoAnswerExist
    |   (list_answer_item | list_item)+     # AnswerExist
    ;


list_item
    :   list_prefix content feedback?
    ;

list_answer_item
    :   answer_prefix content feedback?
    ;

end_answers_list_item
    :   question_prefix content feedback?
    ;

question_prefix
    :   QUESTION_PREFIX
    ;

list_prefix
    :   LIST_PREFIX
    ;

answer_prefix
    :   RIGHT_ANSWER_AFTER
    |   RIGHT_ANSWER_BEFORE
    ;

feedback
    :   FEEDBACK_MARKER content
    ;

end_answers_start
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

FEEDBACK_MARKER
    :   NEWLINE+ BLOCKQUOTE? WHITESPACE* ATSYMBOL WHITESPACE*
    ;
    
END_ANSWERS
    :   NEWLINE+ WHITESPACE* A N S W E R S? WHITESPACE* COLON WHITESPACE*
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

HYPERLINK
    : WHITESPACE* '!' OPEN_BRACKET CHAR* CLOSE_BRACKET '(' CHAR* ')'
    ;

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

