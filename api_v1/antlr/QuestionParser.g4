parser grammar QuestionParser;
options {
	tokenVocab = QuestionLexer;
}

parse_question
    :   question* EOF
    ;

question
    :   start_question question_header question_body answer_list
    |   start_question question_header question_body
    ;

start_question
    :   START_QUESTION
    ;

question_header
    :   question_type? title? points? randomize?
    |   question_type? title? randomize? points?
    |   question_type? points? title? randomize?
    |   question_type? points? randomize? title?
    |   question_type? randomize? title? points?
    |   question_type? randomize? points? title?
    |   title? question_type? points? randomize?
    |   title? question_type? randomize? points?
    |   title? points? question_type? randomize?
    |   title? points? randomize? question_type?
    |   title? randomize? question_type? points?
    |   title? randomize? points? question_type?
    |   points? question_type? title? randomize?
    |   points? question_type? randomize? title?
    |   points? title? question_type? randomize?
    |   points? title? randomize? question_type?
    |   points? randomize? question_type? title?
    |   points? randomize? title? question_type?
    |   randomize? question_type? title? points?
    |   randomize? question_type? points? title?
    |   randomize? title? question_type? points?
    |   randomize? title? points? question_type?
    |   randomize? points? question_type? title?
    |   randomize? points? title? question_type?
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

points
    :   POINTS
    ;

randomize
    :   RANDOMIZE_TRUE      # RandomTrue
    |   RANDOMIZE_FALSE     # RandomFalse
    ;

question_body
    :   question_prefix content+ feedback?
    ;

question_prefix
    :   QUESTION_PREFIX
    ;
    
content
    :   MEDIA                                                           # Media
    |   HYPERLINK                                                       # Hyperlink
    |   ESCAPED_OPEN_BRACKET ALL_CHARACTER+ ESCAPED_CLOSE_BRACKET       # FibAnswer
    |   ALL_CHARACTER+                                                  # ContentCharacters
    ;

feedback
    :   FEEDBACK_MARKER content+
    ;
    
answer_list
    :   START_ANSWER list_item+                              # ListNoAnswer
    |   START_ANSWER (list_answer_item | list_item)+         # ListWithAnswer
    ;

list_item
    :   list_prefix content+ feedback?
    ;

list_prefix
    :   LIST_PREFIX
    ;

list_answer_item
    :   answer_prefix content+ feedback?
    ;

answer_prefix
    :   RIGHT_ANSWER
    ;
