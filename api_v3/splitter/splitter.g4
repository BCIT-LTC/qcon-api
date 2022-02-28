// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar splitter;

// splitter: first_question? questions+  EOF;
splitter: first_question? questions+ EOF;

// extra: ALL_CHARACTER+;

// first_question: NUM_LIST_ONE content | first_question content ;

questions: question_header? START_OF_QUESTION content;

// first_question: content? NUM_LIST_ONE content;

question_header: question_header_parameter+;   

question_header_parameter
    :   points content
    |   title content
    |   questiontype content
    |   randomize content
    ;

title:   TITLE;
points:   POINTS;
questiontype: TYPE;
randomize:   RANDOMIZE;

first_question: ALL_CHARACTER+;

content: ALL_CHARACTER+;

// ================================ TOKENS
// fragment DIGIT: [0-9];
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
// fragment LETTER: [a-zA-Z];
// fragment NUMBER: DIGIT+ (DIGIT+)? (DIGIT+)?;
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment GREATER_THAN: '>';
fragment COLON:   ':';
fragment A:   'A' | 'a';
fragment B:   'B' | 'b';
fragment C:   'C' | 'c';
fragment D:   'D' | 'd';
fragment E:   'E' | 'e';
fragment F:   'F' | 'f';
fragment I:   'I' | 'i';
fragment K:   'K' | 'k';
fragment L:   'L' | 'l';
fragment M:   'M' | 'm';
fragment N:   'N' | 'n';
fragment O:   'O' | 'o';
fragment P:   'P' | 'p';
fragment R:   'R' | 'r';
fragment S:   'S' | 's';
fragment T:   'T' | 't';
fragment U:   'U' | 'u';
fragment W:   'W' | 'w';
fragment Y:   'Y' | 'y';  
fragment Z:   'Z' | 'z';  

fragment EXCLUDE_1: [2-9];
fragment INCLUDE_1: '1';
fragment ZERO: '0';

fragment EXCLUDE_ONE: EXCLUDE_1 | (INCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+ ) | (EXCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+);

fragment NEWLINE_ADDED: '<!-- NewLine -->';
fragment START_OL: '<!-- START OF OL -->';


fragment NUMLIST_EXCLUDE_1_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? EXCLUDE_ONE WHITESPACE* DELIMITER WHITESPACE*;

START_OF_QUESTION: NEWLINE_ADDED NEWLINE* START_OL? NEWLINE* NUMLIST_EXCLUDE_1_PREFIX;

TITLE:  NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T I T L E S? WHITESPACE* ;
POINTS:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* P O I N T S? WHITESPACE*  ;
TYPE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T Y P E S? WHITESPACE*;
RANDOMIZE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE*;

ALL_CHARACTER: .;

