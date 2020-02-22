prefix ()
{
    for file in *.*.*
    do
        echo ${file%%.*} # result of expansion is the value of parameter "file" with the longest matching pattern deleted
    done | sort -u
}

prefix | while read prefix
do
    mkdir -p "$prefix" &&
    mv "$prefix"* "$prefix"/
done
