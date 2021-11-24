import project


def run(args):
    if not project.ensure_loaded():
        return

    if args:
        # todo: write error msg
        print('error')
    for file in project.files:
        print(file)


def documentation():
    print('syntax: files')
