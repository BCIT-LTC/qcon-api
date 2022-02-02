// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar formatter;

formatter: unused_content? body? end_answers? EOF;

unused_content: (ALL_CHARACTER+);

body: body_with_heading_1;

body_with_heading_1: (HEADING_1) (ALL_CHARACTER+);

// body_without_heading_1: NUMBER_ONE (ALL_CHARACTER+);

end_answers: END_ANSWER_BLOCK ALL_CHARACTER+ ;

// ================================ TOKENS
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment COLON:   ':';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment A:   'A' | 'a';
fragment N:   'N' | 'n';
fragment S:   'S' | 's';
fragment W:   'W' | 'w';
fragment E:   'E' | 'e';
fragment R:   'R' | 'r';

fragment ANSWER: A N S W E R (S)?;

// HASH: '#';
// DOUBLE_HASH: '##';

// START_OF_LIST: '<!-- START OF OL -->' | '<!-- START OF BL -->';
// END_OF_LIST: '<!-- END OF OL -->' | '<!-- END OF BL -->';

HEADING_1: NEWLINE '#' WHITESPACE;
// SECTION_HEADING: NEWLINE DOUBLE_HASH;

// START_NUMBER_ONE: NEWLINE '1' WHITESPACE* DELIMITER;

// END_ANSWERS: NEWLINE WHITESPACE* A N S W E R (S)? WHITESPACE* COLON WHITESPACE*;

// END_OF_QUESTIONS: NEWLINE 

// NUMBER_ONE: NEWLINE WHITESPACE* DOUBLE_ASTERISK? '1' WHITESPACE* DELIMITER WHITESPACE*;

END_ANSWER_BLOCK: NEWLINE WHITESPACE* ANSWER WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;