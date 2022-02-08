// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar sectioner;

sectioner: section+ EOF;

section:
	ALL_CHARACTER+ SECTION_START
	| ALL_CHARACTER+ SECTION_END
	| SECTION_START ALL_CHARACTER+
	| ALL_CHARACTER+;
// marked_section: SECTION_START CONTENT+ SECTION_END; unmarked_section: CONTENT+;

// section_title: HEADING CONTENT;

// section_title: TITLE; section: SECTION_START section_title ALL_CHARACTER+ SECTION_END;

// ================================ TOKENS
fragment NEWLINE: ('\r'? '\n' | '\r');
fragment BACKSLASH: '\\';
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

SECTION_START:
	NEWLINE (HASH | DOUBLE_HASH)? WHITESPACE* HASH S E C T I O N WHITESPACE*;
SECTION_END:
	NEWLINE (HASH | DOUBLE_HASH)? WHITESPACE* '/' S E C T I O N WHITESPACE*;

// HEADING: NEWLINE (HASH | DOUBLE_HASH) WHITESPACE;
// ALL_EXCEPT_NEWLINE: ~('\n');
// MARKED_SECTION: SECTION_START ALL_CHARACTER+ SECTION_END;
// TITLE: HEADING ALL_CHARACTER+ NEWLINE;
// CONTENT: NEWLINE ((~'#'))|((~'/'))+ NEWLINE;

ALL_CHARACTER: .;