import os
import project


# COMMAND "INTERFACE"

def run(args):
    if not project.ensure_loaded():
        return

    if not args:
        # todo: write error msg
        print('error')
        return

    if len(args) == 1:
        interpret_filepath(args[0], False)
    elif len(args) == 2:
        option = args[0]
        if option == '-recursive':
            add_recursive(args[0], False)
        elif option == '-verbose':
            interpret_filepath(args[1], True)
        else:
            # todo: write error msg
            print('error')
    elif len(args) == 3 and args[0] == '-recursive' and args[1] == '-verbose':
        add_recursive(args[2], True)
    else:
        # todo: write error msg
        print('error')


def documentation():
    print('syntax: add [-recursive] [-verbose] <filepath>')


# IMPLEMENTATION

def interpret_filepath(filepath, verbose):
    if filepath.endswith('*'):
        directory = filepath[:filepath.rfind('*')]
        if not directory:
            directory = './'
        add_multiple(directory, verbose)
    else:
        add_single(filepath, verbose)


def add_single(filepath, verbose):
    if os.path.isfile(filepath):
        project.files.append(filepath)
        if verbose:
            print(f'added {os.path.abspath(filepath)}')
        print('added 1 file')
    else:
        print('invalid filepath')


def add_multiple(directory, verbose):
    paths = tuple(os.listdir(directory))
    if not paths:
        print('the specified directory is empty')
        return

    files = set()
    for p in paths:
        if os.path.isfile(p):
            files.add(p)
    if not files:
        print('the specified directory only contains subdirectories\n'
              'to add a directory with all its subdirectories'
              'use the \'-recursive\' option, see \'help add\'')
        return

    present = sorted(files.intersection(project.files))
    new = sorted(files.difference(project.files))
    project.files.update(new)

    if verbose:
        print(f'checked these {len(paths)} paths:')
        for p in paths:
            print(f'  {os.path.abspath(directory + p)}')
        if new:
            print(f'added these {len(files)} files:')
            for f in files:
                print(f'  {os.path.abspath(f)}')
            if present:
                print(f'{len(present)} files were already added')
        else:
            print('no files were added\n'
                  f'these {len(present)} files were already added:')
            for f in present:
                print(f'  {os.path.abspath(f)}')
    else:
        if new:
            print(f'added {len(new)} files')
        else:
            print('no files were added\n'
                  f'{len(present)} files were already added')


def add_recursive(directory, verbose):
    # todo: recursive add
    print('not implemented')
