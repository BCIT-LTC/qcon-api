// # This Source Code Form is subject to the terms of the Mozilla Public
// # License, v. 2.0. If a copy of the MPL was not distributed with this
// # file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar formatter;

formatter: rootheading? rootbody end_answers_block? EOF;

rootheading: content;

rootbody: section+;

// sectionlist: sectionheader? rootlist*;

section: sectionheader? sectionbody;

sectionbody: rootlist+;

// rootlist*;

rootlist: question_header? (numlist | letterlist)  wr_answers_block?;

numlist: NUMLIST_PREFIX content;
letterlist: (letterlist_prefix_regular|letterlist_prefix_correct) content;
question_header: question_header_parameter+;     


letterlist_prefix_regular: LETTERLIST_PREFIX;
letterlist_prefix_correct: STAR_AFTER_DOT|STAR_BEFORE_DOT|STAR_BEFORE_LETTER;

// endoflist: ENDOFLIST;


question_header_parameter
    :   points content
    |   title content
    |   questiontype content
    |   randomize content
    ;

end_answers_block
    :   end_answer_token end_answers_item*
    ;
wr_answers_block
    :   wr_answer_token content
    ;

sectionheader
    : SECTION
    ;

end_answer_token
    :   END_ANSWER
    ;

wr_answer_token
    :   WR_ANSWER
    ;

end_answers_item
    :  content? numlist
    ;

title:   TITLE;
points:   POINTS;
questiontype: TYPE;
randomize:   RANDOMIZE;

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

// ENDOFLIST: '<!-- -->' NEWLINE;

fragment WR_ANSWER_FRAGMENT_QCON: A N S W E R WHITESPACE* K E Y;
fragment WR_ANSWER_FRAGMENT_RESPONDUS: C O R R E C T WHITESPACE* A N S W E R S?;
// TODO
// NEWLINE : NEWLINE;
// BLOCKQUOTE: NEWLINE WHITESPACE* GREATER_THAN {setText("\n");}; 
// BLOCKQUOTE: NEWLINE WHITESPACE* GREATER_THAN; 


NUMLIST_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? NUMBER WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

LETTERLIST_PREFIX: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? LETTER LETTER? WHITESPACE* WHITESPACE* DELIMITER WHITESPACE*;

STAR_AFTER_DOT: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? LETTER LETTER? WHITESPACE* DELIMITER WHITESPACE* ANSWER_MARKER WHITESPACE*;
STAR_BEFORE_DOT: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? LETTER LETTER? WHITESPACE* ANSWER_MARKER WHITESPACE* DELIMITER WHITESPACE*;
STAR_BEFORE_LETTER: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* DOUBLE_ASTERISK? ANSWER_MARKER WHITESPACE* LETTER LETTER? WHITESPACE* DELIMITER WHITESPACE*;

TITLE:  NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T I T L E S? WHITESPACE* ;
POINTS:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* P O I N T S? WHITESPACE*  ;
TYPE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* T Y P E S? WHITESPACE*;
RANDOMIZE:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* R A N D O M (I Z E)? (S | D)? WHITESPACE*;
// WR_ANSWER:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R WHITESPACE* K E Y COLON WHITESPACE*;
WR_ANSWER:   NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* (WR_ANSWER_FRAGMENT_QCON | WR_ANSWER_FRAGMENT_RESPONDUS) COLON WHITESPACE*;
END_ANSWER: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R (S)? WHITESPACE* COLON WHITESPACE*;

SECTION: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* S E C T I O N? WHITESPACE* COLON WHITESPACE*;

ALL_CHARACTER: .;