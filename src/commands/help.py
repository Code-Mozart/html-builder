import commands.add
import commands.files
import commands.dir


def run(args):
    if len(args) > 1:
        # todo: write error msg
        print('error')
        return
    command = args[0] if args else None

    if not command:
        all_commands = sorted(('exit', 'help', 'add', 'files', 'dir'))
        for command in all_commands:
            print(command)
    elif command == 'exit':
        exit_documentation()
    elif command == 'help':
        documentation()
    elif command == 'add':
        commands.add.documentation()
    elif command == 'files':
        commands.files.documentation()
    elif command == 'dir':
        commands.dir.documentation()


def documentation():
    print('syntax: help [<command>]\n'
          '\'help\' can either be called in general or for a specific command.\n'
          'Without the additional argument it prints a list of all commands.\n'
          'To get the documentation for a specific command on this list\n'
          'simply type \'help <the command>\'.\n'
          'With a specific command as argument \'help\' prints the documentation\n'
          'for this command, similar to this documentation for the \'help\' command.')


def exit_documentation():
    print('syntax: exit\n'
          'Exits from the application.\n'
          'All changes are immediately auto-saved so there is no need\n'
          'and therefore no option to manually save before exiting.')
