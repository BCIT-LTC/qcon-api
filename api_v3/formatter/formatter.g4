// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar formatter;

formatter: rootheader? body EOF;

rootheader: (ALL_CHARACTER+);

body : body ((SECTION_HEADING ALL_CHARACTER+)? NUMBER_ONE (ALL_CHARACTER+)) |
    ((SECTION_HEADING ALL_CHARACTER+)? NUMBER_ONE (ALL_CHARACTER+)) ;

// ================================ TOKENS
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);

fragment DOUBLE_HASH: '##';
fragment ONE: '1';

NUMBER_ONE: NEWLINE WHITESPACE* DOUBLE_ASTERISK? ONE WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

SECTION_HEADING: NEWLINE DOUBLE_HASH;

ALL_CHARACTER: .;