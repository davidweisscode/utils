#!/bin/bash

# Rename all files in current directory with format "IMG-20180322-123.jpg"
printf "[START] Change file names\n"

# Iterate over all files (jpg, JPG, jpeg, ...)
for file in *
do
    # Rename files --> mv
    # Check against regex and substitute underscore(hyphen) and PANO(IMG) --> sed
    mv -v $file $(echo $file | sed 's/_/-/g; s/PANO/IMG/g')
done

printf "[END] Change file names\n"
