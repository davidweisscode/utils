#!/bin/bash

# Rename all files in current directory
# "IMG-yyyymmdd-123001-123.jpg" --> "yyyymmdd_123001_123.jpg"

printf "[START] Rename images\n\n"

for file in *
do
    new_name=$file
    new_name=$(echo $new_name | sed "s/.*/\L&/") # lower case
    new_name=$(echo $new_name | sed "s/ /-/g")
    new_name=$(echo $new_name | sed "s/_/-/g")
    new_name=$(echo $new_name | sed "s/pxl//g")
    new_name=$(echo $new_name | sed "s/img//g")
    new_name=$(echo $new_name | sed "s/whatsapp//g")
    new_name=$(echo $new_name | sed "s/telegram//g")
    new_name=$(echo $new_name | sed "s/image//g")
    new_name=$(echo $new_name | sed "s/video//g")
    new_name=$(echo $new_name | sed "s/photo//g")
    new_name=$(echo $new_name | sed "s/screenshot//g")
    new_name=$(echo $new_name | sed "s/night//g")
    new_name=$(echo $new_name | sed "s/portrait//g")
    new_name=$(echo $new_name | sed "s/^_//")
    new_name=$(echo $new_name | sed "s/^-//")
    # new_name=$(echo $new_name | sed -E 's,([0-9]{2}).([0-9]{2}).([0-9]{2}),20\3\2\1,g')
    mv -v $file $new_name
done

printf "\n[END] Rename images\n"