#!/bin/bash

# Rename all files in current directory
# "IMG-yyyymmdd-123001-123.jpg" --> "yyyymmdd_123001_123.jpg"

printf "[START] Rename images\n\n"

for file in *
do
    new_name=$file
    new_name=$(echo $new_name | sed "s/ //g")
    new_name=$(echo $new_name | sed "s/-/_/g")
    new_name=$(echo $new_name | sed "s/PXL_//g")
    new_name=$(echo $new_name | sed "s/IMG_//g")
    mv -v $file $new_name
done

printf "\n[END] Rename images\n"
