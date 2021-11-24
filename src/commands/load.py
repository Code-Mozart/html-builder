import os

import parser
import project

proj_file_extension = '.htmlbuilder'


# COMMAND "INTERFACE"

def run(args):
    if len(args) != 1:
        # todo: write error msg
        print('error')
        return

    filepath = args[0]
    if not os.path.exists(filepath):
        print(f'the specified filepath \'{filepath}\' does not exist')
        return

    # if os.path.isfile(filepath) and not filepath.endswith(proj_file_extension):
    #     print(f'the specified file is not a html builder project file')
    #     return
    # elif os.path.isdir(filepath) and not filepath.endswith(proj_file_extension):
    #     directory = filepath
    #     candidates = set()
    #     for p in os.listdir(filepath):
    #         f = directory + p
    #         if os.path.isfile(f) and f.endswith(proj_file_extension):
    #             candidates.add(f)
    #     if not candidates:
    #         print(f'the specified directory \'{directory}\' does not contain a html builder project file')
    #         return
    #     elif len(candidates) > 1:
    #         print(f'the specified directory \'{directory}\' contains multiple html builder project files')
    #         return
    #     else:
    #         filepath = candidates.pop()
    #         print(f'found the html builder project file \'{filepath}\'')
    with open(filepath, 'r') as reader:
        print(f'[content of proj file]')
        parser.map(reader.read())


def documentation():
    print('syntax: load <filepath>')


# IMPLEMENTATION
