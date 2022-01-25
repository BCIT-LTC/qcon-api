// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar sectioner;

sectioner: section+ EOF;

section: section_name? section_body section_answers?
        ;

section_name: SECTION_HEADING ALL_CHARACTER+;

section_body: section_body NUMBER_ONE (ALL_CHARACTER+) |
            NUMBER_ONE (ALL_CHARACTER+);

section_answers: SECTION_ANSWERS (ALL_CHARACTER+) NUMBER_ONE (ALL_CHARACTER+);

// ================================ TOKENS
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment BACKSLASH: '\\';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment GREATER_THAN: '>';
fragment COLON:   ':';
fragment A:   'A' | 'a';
fragment N:   'N' | 'n';
fragment S:   'S' | 's';
fragment W:   'W' | 'w';
fragment E:   'E' | 'e';
fragment R:   'R' | 'r';

fragment DOUBLE_HASH: '##';
fragment ONE: '1';

NUMBER_ONE: NEWLINE WHITESPACE* DOUBLE_ASTERISK? ONE WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

SECTION_HEADING: NEWLINE DOUBLE_HASH;
SECTION_ANSWERS: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R (S)? WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;