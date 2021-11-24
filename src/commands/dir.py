import os


def run(args):
    if len(args) > 1:
        # todo: write error msg
        print('error')
    directory = args[0] if args else './'

    dirs = sorted(tuple(filter(lambda p: os.path.isdir(directory + p), os.listdir(directory))))
    files = sorted(tuple(filter(lambda p: os.path.isfile(directory + p), os.listdir(directory))))

    if dirs:
        print('directories:')
        for d in dirs:
            print(f'  {d}')
    if files:
        print('files:')
        for f in files:
            print(f'  {f}')


def documentation():
    print('syntax: dir [<filepath>]')
