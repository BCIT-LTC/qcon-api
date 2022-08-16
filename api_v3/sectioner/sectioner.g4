// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar sectioner;

sectioner: section+ EOF;

title: HEADING;

section:
	SECTION_START unused_content? title? sectiontext? sectioncontent SECTION_END
	| unused_content? maincontent | unused_content;

unused_content: ALL_CHARACTER+;

sectiontext: ALL_CHARACTER+;
sectioncontent:
	QUESTION_PREFIX ALL_CHARACTER+
	| sectioncontent QUESTION_PREFIX ALL_CHARACTER+;

maincontent: QUESTION_PREFIX ALL_CHARACTER+
	| sectioncontent QUESTION_PREFIX ALL_CHARACTER+;

// ================================ TOKENS
fragment NEWLINE: ('\r'? '\n' | '\r');
fragment WHITESPACE: ' ' | '\t';
fragment DIGIT: [0-9];
fragment NUMBER: DIGIT+ (DIGIT+)?;
fragment CLOSING_PARENTHESIS: ')';
fragment BACKSLASH: '\\';
fragment DOT: '.';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment S: 'S' | 's';
fragment E: 'E' | 'e';
fragment C: 'C' | 'c';
fragment T: 'T' | 't';
fragment I: 'I' | 'i';
fragment O: 'O' | 'o';
fragment N: 'N' | 'n';

fragment HASH: '#';
fragment DOUBLE_HASH: '##';

fragment HEADING_START: (HASH | DOUBLE_HASH) WHITESPACE;

QUESTION_PREFIX:
	NEWLINE WHITESPACE* DOUBLE_ASTERISK? NUMBER WHITESPACE* DELIMITER WHITESPACE*;

SECTION_START:
	NEWLINE ((HASH | DOUBLE_HASH)? WHITESPACE)? (ASTERISK|DOUBLE_ASTERISK)? HASH S E C T I O N WHITESPACE* (ASTERISK|DOUBLE_ASTERISK)? NEWLINE+;
SECTION_END:
	NEWLINE ((HASH | DOUBLE_HASH)? WHITESPACE)? (ASTERISK|DOUBLE_ASTERISK)? '/' S E C T I O N WHITESPACE* (ASTERISK|DOUBLE_ASTERISK)?; 

HEADING: HEADING_START (~'#' | ~'\n') .*? NEWLINE;

ALL_CHARACTER: .;
