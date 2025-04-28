#!/bin/awk -f

{
    # split fields using ";" instead of TAB
    gsub(/ *\t+ */, ";")

    # remove some numbers, mostly used for allergens
    gsub(/[0-9]+, */, "")
    # remove all weigths
    gsub(/Gr\. *[0-9]+/, "")
    # remove all remaining numbers
    gsub(/ *[0-9]/, "")

    # use ASCII accent char
    gsub(/’/, "`")

    # improve lists by separating each records with "o " and not " o "
    gsub(/ +o +/, "o ")
    # squeeze consecutive spaces
    gsub(/ +/, " ")
    # remove trailing spaces, convert CRLF line endings to LF
    sub(/ +\r?$/, "")

    # print result
    print($0)
}
