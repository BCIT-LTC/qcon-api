parser grammar QuestionParser;
options {
	tokenVocab = QuestionLexer;
}

parse_question
    :   section_title? question* end_answers? EOF
    ;

section_title
    :   SECTION_TITLE
    ;

question
    :   question_header? start_question question_body answer_list
    |   question_header? start_question question_body
    ;

start_question
    :   START_QUESTION
    ;

question_header
    :   START_QUESTION_HEADER question_type? title? points? randomize?
    |   START_QUESTION_HEADER question_type? title? randomize? points?
    |   START_QUESTION_HEADER question_type? points? title? randomize?
    |   START_QUESTION_HEADER question_type? points? randomize? title?
    |   START_QUESTION_HEADER question_type? randomize? title? points?
    |   START_QUESTION_HEADER question_type? randomize? points? title?
    |   START_QUESTION_HEADER title? question_type? points? randomize?
    |   START_QUESTION_HEADER title? question_type? randomize? points?
    |   START_QUESTION_HEADER title? points? question_type? randomize?
    |   START_QUESTION_HEADER title? points? randomize? question_type?
    |   START_QUESTION_HEADER title? randomize? question_type? points?
    |   START_QUESTION_HEADER title? randomize? points? question_type?
    |   START_QUESTION_HEADER points? question_type? title? randomize?
    |   START_QUESTION_HEADER points? question_type? randomize? title?
    |   START_QUESTION_HEADER points? title? question_type? randomize?
    |   START_QUESTION_HEADER points? title? randomize? question_type?
    |   START_QUESTION_HEADER points? randomize? question_type? title?
    |   START_QUESTION_HEADER points? randomize? title? question_type?
    |   START_QUESTION_HEADER randomize? question_type? title? points?
    |   START_QUESTION_HEADER randomize? question_type? points? title?
    |   START_QUESTION_HEADER randomize? title? question_type? points?
    |   START_QUESTION_HEADER randomize? title? points? question_type?
    |   START_QUESTION_HEADER randomize? points? question_type? title?
    |   START_QUESTION_HEADER randomize? points? title? question_type?
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

end_answers
    :   END_ANSWERS end_answers_item+
    ;

end_answers_item
    :   question_prefix content+ feedback?
    ;