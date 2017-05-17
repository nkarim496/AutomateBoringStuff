"""Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string."""

import re

def striper(string, symbol=" "):
    pattern_begin = '^' + symbol + '+'
    string = re.sub(pattern_begin, '', string)

    pattern_end = symbol + '+$'
    string = re.sub(pattern_end,'', string)

    return string

inputs = [
    'Kolya ',
    '  manna',
    ' Russia',
    '   Family',
    'MMA   ',
    '  Rrrra dabadaaa'
    ]

for inp in inputs:
    print(striper(inp))
