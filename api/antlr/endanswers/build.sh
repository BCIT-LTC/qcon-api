# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

#!/bin/bash

FILE="endanswers"
ANTLR=$(echo $CLASSPATH | tr ':' '\n' | grep -m 1 "antlr-4.9.3-complete.jar")
java -jar $ANTLR $FILE.g4 -visitor -no-listener
javac $FILE*.java

# grun endanswers endanswers -gui test.txt -tokens
