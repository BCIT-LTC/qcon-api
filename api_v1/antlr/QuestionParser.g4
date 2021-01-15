parser grammar QuestionParser;
options {
	tokenVocab = QuestionLexer;
}

parse_question
    :   question EOF
    ;

question
    :   question_header question_body (answers_list | regular_list)     # QuestionWithAnswers
    |   question_header question_body                                   # QuestionWithoutAnswers
    ;

question_body
    :   question_prefix regular_list* content+ regular_list* feedback?
    ;

question_header
    :   question_type? title? points?
    |   title? question_type? points?
    |   points? question_type? title?
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

content
    :   MEDIA                                                           # Media
    |   ESCAPED_OPEN_BRACKET ALL_CHARACTER+ ESCAPED_CLOSE_BRACKET       # FibAnswer
    |   HYPERLINK                                                       # Hyperlink
    // |   regular_list                                                    # NormalList
    |   ALL_CHARACTER+                                                  # ContentCharacters
    ;

regular_list
    :   list_item+
    ;

answers_list
    :   (list_item | list_item_feedback | list_answer_item)+
    ;

list_item_feedback
    :   list_prefix content+ feedback
    ;

list_item
    :   list_prefix content+
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
    :   RIGHT_ANSWER_AFTER
    |   RIGHT_ANSWER_BEFORE
    ;

feedback
    :   FEEDBACK_MARKER content+
    ;