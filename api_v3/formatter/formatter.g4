// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar formatter;

formatter: unused_content? sectioninfo? body end_answers? EOF;

unused_content: (ALL_CHARACTER+);

sectioninfo:
	sectioninfo (HEADING_1 | HEADING_2) (ALL_CHARACTER+)
	| (HEADING_1 | HEADING_2) (ALL_CHARACTER+);

body:
	body question_header_parameter* START_NUMBER_ONE (ALL_CHARACTER+ | question_header_parameter*)
	| question_header_parameter* START_NUMBER_ONE (ALL_CHARACTER+ question_header_parameter*) body
    | question_header_parameter* START_NUMBER_ONE (ALL_CHARACTER+ question_header_parameter*)
    | (HEADING_1 | HEADING_2) (ALL_CHARACTER+ question_header_parameter*) body;

question_header_parameter:
	TITLE ALL_CHARACTER+ | POINTS ALL_CHARACTER+ | TYPE ALL_CHARACTER+ | RANDOMIZE ALL_CHARACTER+;

end_answers: END_ANSWER_BLOCK ALL_CHARACTER+ START_NUMBER_ONE ALL_CHARACTER+;

// ================================ TOKENS
fragment NEWLINE: ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment COLON: ':';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
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

fragment ANSWER: A N S W E R (S)?;

fragment HASH: '#';
fragment DOUBLE_HASH: '##';

START_OL: (NEWLINE WHITESPACE* '<!-- START OF OL -->') -> skip;
END_OL: (NEWLINE WHITESPACE* '<!-- END OF OL -->') -> skip;

HEADING_1: NEWLINE '#' WHITESPACE;
HEADING_2: NEWLINE '##' WHITESPACE;
START_NUMBER_ONE: NEWLINE '1' WHITESPACE* DELIMITER;

END_ANSWER_BLOCK:
	NEWLINE WHITESPACE* ANSWER WHITESPACE* COLON WHITESPACE*;

TITLE:  NEWLINE WHITESPACE* WHITESPACE* T I T L E S? WHITESPACE*;
POINTS:   NEWLINE WHITESPACE* WHITESPACE* P O I N T S? WHITESPACE*;
TYPE:   NEWLINE WHITESPACE* WHITESPACE* T Y P E S? WHITESPACE*;
RANDOMIZE:   NEWLINE WHITESPACE* WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE*;

ALL_CHARACTER: .;