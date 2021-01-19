parser grammar QuestionParser;
options {
	tokenVocab = QuestionLexer;
}

parse_question
    :   question EOF
    ;

question
    :   question_header question_body answers_list                      # QuestionWithAnswers
    |   question_header question_body                                   # QuestionWithoutAnswers
    ;

question_body
    :   question_prefix content+ feedback?
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

content
    :   MEDIA                                                           # Media
    |   HYPERLINK                                                       # Hyperlink
    |   ESCAPED_OPEN_BRACKET ALL_CHARACTER+ ESCAPED_CLOSE_BRACKET       # FibAnswer
    |   ALL_CHARACTER+                                                  # ContentCharacters
    ;

answers_list
    :   START_ANSWER list_item+ END_ANSWER                              # ListNoAnswer  
    |   START_ANSWER (list_answer_item | list_item)+ END_ANSWER         # ListWithAnswer
    ;

list_item
    :   list_prefix content+ feedback?
    ;

list_answer_item
    :   answer_prefix content+ feedback?
    ;

question_prefix
    :   QUESTION_PREFIX
    ;

list_prefix
    :   LIST_PREFIX
    ;

answer_prefix
    :   RIGHT_ANSWER
    ;

feedback
    :   FEEDBACK_MARKER content+
    ;