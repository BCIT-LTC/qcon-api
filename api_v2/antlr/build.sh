# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
 
 #!/bin/bash

FILE="Qcon"
ANTLR=$(echo $CLASSPATH | tr ':' '\n' | grep -m 1 "antlr-4.8-complete.jar")
java -jar $ANTLR $FILE.g4
javac $FILE*.java

# grun Qcon qcon -gui test.txt -tokens

# antlr4 -Dlanguage=Python3 -visitor Qcon.g4