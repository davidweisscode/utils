#!/bin/bash

# Copies content of all directories in current directory
# into the current directory
printf "[START] Copy out files\n"

for dir in *
  do
  	if [ -d $dir ]
      then
        printf $dir/*
        printf "\n"
        cp $dir/* .
    fi
  done

printf "[END] Copy out files\n"
