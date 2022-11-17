// # This Source Code Form is subject to the terms of the Mozilla Public # License, v. 2.0. If a
// copy of the MPL was not distributed with this # file, You can obtain one at
// https://mozilla.org/MPL/2.0/.

grammar formatter;

formatter: maincontent_title? body end_answers? EOF;

maincontent_title: (ALL_CHARACTER+);

body:
    sectioninfo? question_header_parameter* START_NUMBER_ONE (ALL_CHARACTER+ question_header_parameter*)
	| body sectioninfo? question_header_parameter* (ALL_CHARACTER+ question_header_parameter*)
    | question_header_parameter* START_NUMBER_ONE (ALL_CHARACTER+ question_header_parameter*) sectioninfo? body sectioninfo?;
    // | sectioninfo? (ALL_CHARACTER+ question_header_parameter*) sectioninfo? body sectioninfo?;
    // | sectioninfo? question_header_parameter* START_NUMBER_ONE? (ALL_CHARACTER+ | question_header_parameter*) body;

sectioninfo:
     SECTION_START (ALL_CHARACTER+);

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
fragment HEADING_1: NEWLINE (ASTERISK|DOUBLE_ASTERISK)? HASH WHITESPACE;
fragment HEADING_2: NEWLINE (ASTERISK|DOUBLE_ASTERISK)? DOUBLE_HASH WHITESPACE;

// SECTION_START: NEWLINE HASH S E C T I O N WHITESPACE* NEWLINE (HEADING_1 | HEADING_2)?;
SECTION_START:
	NEWLINE ((HASH | DOUBLE_HASH)? WHITESPACE)? (ASTERISK|DOUBLE_ASTERISK)? HASH S E C T I O N WHITESPACE* (ASTERISK|DOUBLE_ASTERISK)? NEWLINE+ (HEADING_1 | HEADING_2)?;

// START_OL: (NEWLINE WHITESPACE* '<!-- START OF OL -->') -> skip;
// END_OL: (NEWLINE WHITESPACE* '<!-- END OF OL -->') -> skip;
START_NUMBER_ONE: NEWLINE '1' WHITESPACE* DELIMITER;

END_ANSWER_BLOCK:
    NEWLINE WHITESPACE* ANSWER WHITESPACE* COLON WHITESPACE*;

TITLE:  NEWLINE WHITESPACE* WHITESPACE* T I T L E S? WHITESPACE*;
POINTS:   NEWLINE WHITESPACE* WHITESPACE* P O I N T S? WHITESPACE*;
TYPE:   NEWLINE WHITESPACE* WHITESPACE* T Y P E S? WHITESPACE*;
RANDOMIZE:   NEWLINE WHITESPACE* WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE*;

ALL_CHARACTER: .;