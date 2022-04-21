// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar questionparser;

questionparser: question_wrapper answers? trailing_content EOF;

question_wrapper: (question | fib_question);

question: content;

fib_question: (fib_part content)* | (content fib_part)* | (fib_part)*;

// fib_question: ((fib_part content) fib_question)
// 			| ((content fib_part) fib_question)
// 			| (fib_part  content)
// 			| (content fib_part)
// 			| fib_part
// 			| content;

fib_part: FIB_START ALL_CHARACTER* FIB_END;
answers:
	START_OL? ((answer_part | correct_answer_part)+ | wr_answer) END_OL?;
answer_part: LETTERLIST_PREFIX content;
correct_answer_part: CORRECT_ANSWER content;

wr_answer: CORRECT_ANSWER_FOR_WR content;

content: ALL_CHARACTER*;
trailing_content: ALL_CHARACTER*;

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

fragment STAR_AFTER_DOT:
	NEWLINE WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE* ANSWER_MARKER WHITESPACE*;
fragment STAR_BEFORE_DOT:
	NEWLINE WHITESPACE* LETTER WHITESPACE* ANSWER_MARKER WHITESPACE* DELIMITER WHITESPACE*;
fragment STAR_BEFORE_LETTER:
	NEWLINE WHITESPACE* ANSWER_MARKER WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE*;

START_OL: (NEWLINE WHITESPACE* '<!-- START OF OL -->') -> skip;
END_OL: (NEWLINE WHITESPACE* '<!-- END OF OL -->') -> skip;

// NUMLIST_PREFIX: NEWLINE WHITESPACE* NUMBER WHITESPACE* DELIMITER WHITESPACE*;
LETTERLIST_PREFIX:
	NEWLINE WHITESPACE* LETTER WHITESPACE* DELIMITER WHITESPACE*;

FIB_START: OPEN_BRACKET WHITESPACE*;
FIB_END: WHITESPACE* CLOSE_BRACKET;

CORRECT_ANSWER: (
		STAR_AFTER_DOT
		| STAR_BEFORE_DOT
		| STAR_BEFORE_LETTER
	);

CORRECT_ANSWER_FOR_WR:
	NEWLINE WHITESPACE* C O R R E C T WHITESPACE* A N S W E R WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;

