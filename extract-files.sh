#!/bin/bash

# Copies content of all directories in current directory
# into the current directory
printf "[START] Extract files\n"

for dir in *
  do
    if [ -d $dir ]
      then
        ls $dir
        cp $dir/* .
    fi
  done

printf "[END] Extract files\n"
