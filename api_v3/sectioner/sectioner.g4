// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar sectioner;

sectioner: section+ EOF;

title: HEADING;

section: SECTION_START unused_content? title? content SECTION_END | maincontent;

unused_content: ALL_CHARACTER+;

content: ALL_CHARACTER+;

maincontent: ALL_CHARACTER+;

// ================================ TOKENS
fragment NEWLINE: ('\r'? '\n' | '\r');
fragment WHITESPACE: ' ' | '\t';

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

SECTION_START:
	NEWLINE ((HASH | DOUBLE_HASH)? WHITESPACE)? HASH S E C T I O N WHITESPACE* NEWLINE+;
SECTION_END:
	NEWLINE (HASH | DOUBLE_HASH)? WHITESPACE* '/' S E C T I O N WHITESPACE*;

HEADING: HEADING_START (~'#' | ~'\n') .*? NEWLINE;

ALL_CHARACTER: .;