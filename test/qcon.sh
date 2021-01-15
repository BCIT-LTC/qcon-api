#!/bin/bash

echo 'Welcome to Qcon'
read -e -p "Type the path to docx or plain text file: " FILE
echo 'Converting document...'
printf 'Response: '
curl -XPOST -H 'Accept: application/json' "http://127.0.0.1:8000/api/v1/word2question/" -F 'file=@'$FILE