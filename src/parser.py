import re


def map(string):
    words = re.split('[ \n\r]+', string)
    for w in words:
        print(w)


def extract(string, separators=' \n\r', arg_symbols = '""'):
    if len(arg_symbols) != 2:
        raise ValueError('\'arg_symbols\' must specify exactly one character '
                         'for marking the beginning of the argument and one character'
                         'for marking the end of the argument')
    begin_arg = arg_symbols[0]
    end_arg = arg_symbols[1]

    tokens = []
    in_arg = False
    for c in string:
        if in_arg:
            if
