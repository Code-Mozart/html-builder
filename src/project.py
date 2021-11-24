project_name = None
root = None
files = set()

build_dir = None
manifests = set()
default_manifest = None


def ensure_loaded():
    if project_name:
        return True
    else:
        # todo: write error msg
        print('error! load a project first')
        return False


def load(filepath):
    with open(filepath, 'r') as reader:
        tokens = tuple(reader.read().split(' '))
