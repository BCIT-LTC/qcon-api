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
fragment DIGIT: [0-9];
fragment NEWLINE:   ('\r'? '\n' | '\r');
fragment CLOSING_PARENTHESIS: ')';
fragment LETTER: [a-zA-Z];
fragment NUMBER: DIGIT+ (DIGIT+)?;
fragment BACKSLASH: '\\';
fragment ASTERISK: '*';
fragment DOUBLE_ASTERISK: '**';
fragment DOT: '.';
fragment WHITESPACE: ' ' | '\t';
fragment DELIMITER: BACKSLASH? (DOT | CLOSING_PARENTHESIS);
fragment ANSWER_MARKER: BACKSLASH ASTERISK;
fragment GREATER_THAN: '>';
fragment COLON:   ':';
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

fragment DOUBLE_HASH: '##';
fragment ONE: '1';

NUMBER_ONE: NEWLINE WHITESPACE* DOUBLE_ASTERISK? ONE WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

SECTION_HEADING: NEWLINE DOUBLE_HASH;
SECTION_ANSWERS: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R (S)? WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;