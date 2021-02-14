#!/bin/bash

FILE="Qcon"
ANTLR=$(echo $CLASSPATH | tr ':' '\n' | grep -m 1 "antlr-4.8-complete.jar")
java -jar $ANTLR $FILE.g4
javac $FILE*.java

# grun Qcon qcon -gui test.txt -tokens

# antlr4 -Dlanguage=Python3 -visitor Qcon.g4