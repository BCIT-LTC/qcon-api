// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar sectioner;

sectioner: section+ EOF;

title: HEADING;

section:
	SECTION_START unused_content? title? sectiontext? sectioncontent SECTION_END
	| unused_content? maincontent 
	| unused_content;

unused_content: ALL_CHARACTER+;

sectiontext: ALL_CHARACTER+;
sectioncontent:
	QUESTION_PREFIX ALL_CHARACTER+
	| sectioncontent QUESTION_PREFIX ALL_CHARACTER+;

maincontent: question_header_parameter? QUESTION_PREFIX ALL_CHARACTER+
	| maincontent question_header_parameter? QUESTION_PREFIX ALL_CHARACTER+;

question_header_parameter:
	TITLE ALL_CHARACTER+ | POINTS ALL_CHARACTER+ | TYPE ALL_CHARACTER+ | RANDOMIZE ALL_CHARACTER+;

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

TITLE:  NEWLINE WHITESPACE* WHITESPACE* T I T L E S? WHITESPACE*;
POINTS:   NEWLINE WHITESPACE* WHITESPACE* P O I N T S? WHITESPACE*;
TYPE:   NEWLINE WHITESPACE* WHITESPACE* T Y P E S? WHITESPACE*;
RANDOMIZE:   NEWLINE WHITESPACE* WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE*;

ALL_CHARACTER: .;
