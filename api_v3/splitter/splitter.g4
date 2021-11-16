// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar splitter;

splitter: question+ EOF;

question: content;

content: ALL_CHARACTER+;

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

NUMLIST_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? NUMBER WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

END_ANSWER: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R (S)? WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;

