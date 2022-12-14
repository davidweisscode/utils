#!/bin/bash

# Rename all files in current directory
# "IMG-yyyymmdd-123001-123.jpg" --> "yyyymmdd_123001_123.jpg"

printf "[START] Rename images\n\n"

for file in *
do
    new_name=$file
    new_name=$(echo $new_name | sed "s/ //g")
    new_name=$(echo $new_name | sed "s/-/_/g")
    new_name=$(echo $new_name | sed "s/PXL//g")
    new_name=$(echo $new_name | sed "s/IMG//g")
    new_name=$(echo $new_name | sed "s/WhatsApp//g")
    new_name=$(echo $new_name | sed "s/Image//g")
    new_name=$(echo $new_name | sed "s/Video//g")
    new_name=$(echo $new_name | sed "s/Photo//g")
    new_name=$(echo $new_name | sed "s/Screenshot//g")
    new_name=$(echo $new_name | sed "s/^_//")
    # new_name=$(echo $new_name | sed -E 's,([0-9]{2}).([0-9]{2}).([0-9]{2}),20\3\2\1,g')
    mv -v $file $new_name
done

printf "\n[END] Rename images\n"
