#!/bin/bash

FILE="Grammar"
ANTLR=$(echo $CLASSPATH | tr ':' '\n' | grep -m 1 "antlr-4.8-complete.jar")
java -jar $ANTLR $FILE.g4
javac $FILE*.java

# grun Grammar prog -gui test.txt -tokens