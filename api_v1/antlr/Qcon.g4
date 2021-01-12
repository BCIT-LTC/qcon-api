grammar Qcon;



qcon
    :   question* endanswers? EOF
    ;

question
    : fib_question_body           # FibQuestion
    | question_body answerlist   # QuestionWithAnswers
    | question_body              # QuestionWithoutAnswers
    ;

endanswers
    :   end_answers_start end_answers_list_item+
    ;

question_body
    :   question_prefix content+ feedback?
    |   question_type? title? point? question_prefix content feedback?
    |   question_type? point? title? question_prefix content feedback?
    |   title? question_type? point? question_prefix content feedback?
    |   title? point? question_type? question_prefix content feedback?
    |   point? question_type? title? question_prefix content feedback?
    |   point? title? question_type? question_prefix content feedback?
    ;

fib_question_body
    :   question_prefix fib_content+ feedback?
    |   fib_type? title? point? question_prefix fib_content+ feedback?
    |   fib_type? point? title? question_prefix fib_content+ feedback?
    |   title? fib_type? point? question_prefix fib_content+ feedback?
    |   title? point? fib_type? question_prefix fib_content+ feedback?
    |   point? fib_type? title? question_prefix fib_content+ feedback?
    |   point? title? fib_type? question_prefix fib_content+ feedback?
    ;

fib_content
    :   fib_answer 
    |   content
    ;

fib_type
    :   FIB_TYPE
    ;

question_type
    :   TYPE
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
    : HYPERLINK
    | ALL_CHARACTER+
    ;

// list
//     :   (listitem)+ (list+)?
//     ;

answerlist
    :   // answeritem+ (answerlist+)?
    list_item+                         # NoAnswerExist
    | (list_answer_item | list_item)+    # AnswerExist
    ;

// answeritem
//     :   listitem
//     |   listansweritem
//     ;

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
    :   FEEDBACKMARKER content
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

