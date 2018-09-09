#!/usr/bin/env bash


echo "Hello Bash"

if [[ -e access.log ]]; then
    echo "Print access log"
else
    echo "File does not exist"
fi

if [[ -e access.log ]]; then
   echo "THe access File is exist"
   diff -u example.txt access.log > diff.txt
   echo "The Difference will ne written on diff txt file"
else
   cp example.txt diff.txt
   echo "... Done"
fi
