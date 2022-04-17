// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar splitter;

splitter: first_question? questions+ trailing_content? EOF;

first_question: question_header? START_OF_QUESTION_ONE? content;
trailing_content: (content|NEWLINE_ADDED)+ ;

questions:  (NEWLINE_ADDED| NEWLINE_ADDED? question_header)? START_OF_QUESTION_NOT_ONE content;

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


content: ALL_CHARACTER+;

// ================================ TOKENS
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
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

NEWLINE_ADDED: '<!-- NewLine -->' NEWLINE;
fragment START_OL: '<!-- START OF OL -->';

fragment EXCLUDE_ONE: EXCLUDE_1 | (INCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+ ) | (EXCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+);

fragment NUMLIST_EXCLUDE_1_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? EXCLUDE_ONE WHITESPACE* DELIMITER WHITESPACE*;

fragment NUMLIST_INCLUDE_1_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? INCLUDE_1 WHITESPACE* DELIMITER WHITESPACE*;

START_OF_QUESTION_NOT_ONE: NEWLINE* START_OL? NEWLINE* NUMLIST_EXCLUDE_1_PREFIX;
START_OF_QUESTION_ONE: NEWLINE* START_OL? NEWLINE* NUMLIST_INCLUDE_1_PREFIX;

TITLE:  NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T I T L E S? WHITESPACE* COLON;
POINTS:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* P O I N T S? WHITESPACE* COLON;
TYPE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T Y P E S? WHITESPACE* COLON;
RANDOMIZE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE* COLON;

ALL_CHARACTER: .;

