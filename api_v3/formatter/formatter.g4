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
	body START_NUMBER_ONE (ALL_CHARACTER+)
	| START_NUMBER_ONE (ALL_CHARACTER+) body
    | START_NUMBER_ONE (ALL_CHARACTER+)
    | (HEADING_1 | HEADING_2) (ALL_CHARACTER+) body;

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
fragment A: 'A' | 'a';
fragment N: 'N' | 'n';
fragment S: 'S' | 's';
fragment W: 'W' | 'w';
fragment E: 'E' | 'e';
fragment R: 'R' | 'r';

fragment ANSWER: A N S W E R (S)?;

fragment HASH: '#';
fragment DOUBLE_HASH: '##';

HEADING_1: NEWLINE '#' WHITESPACE;
HEADING_2: NEWLINE '##' WHITESPACE;
START_NUMBER_ONE: NEWLINE '1' WHITESPACE* DELIMITER;

END_ANSWER_BLOCK:
	NEWLINE WHITESPACE* ANSWER WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;