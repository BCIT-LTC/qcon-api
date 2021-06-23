# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

grammar L1;

// options 
// {
// output=AST;
// backtrack=true;
// memoize=true;
// }

// @parser::members{
// public class Question {

    
//     }
// }

l1: sectionheading? rootlist* end_answers? EOF;

sectionheading: content;

rootlist: question_header? (numlist | letterlist) endoflist?;

numlist: numlist_prefix content;
letterlist: (letterlist_prefix_regular|letterlist_prefix_correct) content;
question_header: question_header_parameter+;     

numlist_prefix: NUMLIST_PREFIX;

letterlist_prefix_regular: LETTERLIST_PREFIX;
letterlist_prefix_correct: STAR_AFTER_DOT|STAR_BEFORE_DOT|STAR_BEFORE_LETTER;

endoflist: ENDOFLIST;


question_header_parameter
    :   points content
    |   title content
    |   questiontype content
    |   randomize content
    ;

end_answers
    :   END_ANSWER end_answers_item+
    ;

end_answers_item
    :   numlist content+ 
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

ENDOFLIST: '<!-- -->' NEWLINE;

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

END_ANSWER: NEWLINE WHITESPACE* GREATER_THAN? WHITESPACE* A N S W E R (S)? WHITESPACE* COLON NEWLINE*;

// FEEDBACK
// BOLDED_STAR_AFTER_DOT: NEWLINE WHITESPACE* DOUBLE_ASTERISK LETTER LETTER? WHITESPACE* DELIMITER WHITESPACE* ANSWER_MARKER WHITESPACE*;
// BOLDED_STAR_BEFORE_DOT: NEWLINE WHITESPACE* DOUBLE_ASTERISK LETTER LETTER? WHITESPACE* ANSWER_MARKER WHITESPACE* DELIMITER WHITESPACE*;
// BOLDED_STAR_BEFORE_LETTER: NEWLINE WHITESPACE* DOUBLE_ASTERISK ANSWER_MARKER WHITESPACE* LETTER LETTER? WHITESPACE* DELIMITER WHITESPACE*;


ALL_CHARACTER: .;

