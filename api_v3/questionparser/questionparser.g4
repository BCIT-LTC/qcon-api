// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar questionparser;

questionparser: unused_content? question_header? question_wrapper hint? answers wr_answer? EOF;

unused_content: (ALL_CHARACTER+) ;

question_header: question_header_part+;

question_header_part: 
		TITLE content
	|	POINTS content
	|	TYPE content
	|	RANDOMIZE content;

question_wrapper: (NUMLIST_PREFIX_ONE|NUMLIST_PREFIX_NOT_ONE) (question | fib_question);

question: feedback? question_part feedback?;

question_part: content NUMLIST_PREFIX_ONE question_part
	| content NUMLIST_PREFIX_NOT_ONE question_part
	| content NUMLIST_PREFIX_NOT_ONE
	| content NUMLIST_PREFIX_ONE 
	| content;

fib_question: ((fib_part content)* | (content fib_part)* | (fib_part)*) feedback?;
fib_part: FIB_START ALL_CHARACTER* FIB_END;

answers: (answer_part | correct_answer_part)+;
answer_part: LETTERLIST_PREFIX feedback? content feedback?;
correct_answer_part: CORRECT_ANSWER feedback? content feedback?;
wr_answer: CORRECT_ANSWER_FOR_WR content;

hint: HINT content;

feedback: FEEDBACK content;
content: ALL_CHARACTER*;

// ================================ TOKENS
fragment DIGIT: [0-9];
fragment NEWLINE: ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment LETTER: [a-zA-Z];
fragment NUMBER: DIGIT+ (DIGIT+)?;
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment ANSWER_MARKER: BACKSLASH ASTERISK;
fragment COLON: ':';
fragment A: 'A' | 'a';
fragment B: 'B' | 'b';
fragment C: 'C' | 'c';
fragment D: 'D' | 'd';
fragment E: 'E' | 'e';
fragment F: 'F' | 'f';
fragment H: 'H' | 'h';
fragment I: 'I' | 'i';
fragment K: 'K' | 'k';
fragment L: 'L' | 'l';
fragment M: 'M' | 'm';
fragment N: 'N' | 'n';
fragment O: 'O' | 'o';
fragment P: 'P' | 'p';
fragment R: 'R' | 'r';
fragment S: 'S' | 's';
fragment T: 'T' | 't';
fragment U: 'U' | 'u';
fragment W: 'W' | 'w';
fragment Y: 'Y' | 'y';
fragment Z: 'Z' | 'z';
fragment OPEN_BRACKET: '\\[';
fragment CLOSE_BRACKET: '\\]';
fragment AT: '@';

fragment EXCLUDE_1: [2-9];
fragment INCLUDE_1: '1';
fragment ZERO: '0';
fragment NEWLINE_ADDED: '<!-- NewLine -->' NEWLINE;
fragment EXCLUDE_ONE: EXCLUDE_1 | (INCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+ ) | (EXCLUDE_1 (ZERO|INCLUDE_1|EXCLUDE_1)+);
fragment NUMLIST_EXCLUDE_1_PREFIX: NEWLINE WHITESPACE* DOUBLE_ASTERISK? EXCLUDE_ONE WHITESPACE* DELIMITER WHITESPACE*;
fragment NUMLIST_INCLUDE_1_PREFIX: NEWLINE WHITESPACE* DOUBLE_ASTERISK? INCLUDE_1 WHITESPACE* DELIMITER WHITESPACE*;

fragment STAR_AFTER_DELIMITER:
	NEWLINE WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE* ANSWER_MARKER WHITESPACE*;
fragment STAR_BEFORE_DELIMITER:
	NEWLINE WHITESPACE* LETTER WHITESPACE* ANSWER_MARKER WHITESPACE* DELIMITER WHITESPACE*;
fragment STAR_BEFORE_LETTER:
	NEWLINE WHITESPACE* ANSWER_MARKER WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE*;

fragment TITLE_KEYWORD:  NEWLINE WHITESPACE* T I T L E S? WHITESPACE* COLON;
fragment POINTS_KEYWORD:   NEWLINE WHITESPACE* P O I N T S? WHITESPACE* COLON;
fragment TYPE_KEYWORD:   NEWLINE WHITESPACE* T Y P E S? WHITESPACE* COLON;
fragment RANDOMIZE_KEYWORD:   NEWLINE WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE* COLON;

TITLE: TITLE_KEYWORD ;
POINTS: POINTS_KEYWORD ;
TYPE: TYPE_KEYWORD ;
RANDOMIZE: RANDOMIZE_KEYWORD ;

NUMLIST_PREFIX_ONE: NUMLIST_INCLUDE_1_PREFIX;
NUMLIST_PREFIX_NOT_ONE: NUMLIST_EXCLUDE_1_PREFIX;

LETTERLIST_PREFIX:
	NEWLINE WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE*;

FEEDBACK: NEWLINE WHITESPACE* (ASTERISK|DOUBLE_ASTERISK)? AT F E E D B A C K COLON? WHITESPACE*;
HINT: NEWLINE WHITESPACE* (ASTERISK|DOUBLE_ASTERISK)? AT H I N T COLON? WHITESPACE*;
FIB_START: OPEN_BRACKET WHITESPACE*;
FIB_END: WHITESPACE* CLOSE_BRACKET;

CORRECT_ANSWER: (
		STAR_AFTER_DELIMITER
		| STAR_BEFORE_DELIMITER
		| STAR_BEFORE_LETTER
	);

CORRECT_ANSWER_FOR_WR:
	NEWLINE WHITESPACE* C O R R E C T WHITESPACE* A N S W E R WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;