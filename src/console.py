import commands.add
import commands.dir
import commands.files
import commands.help
import commands.load


def interpret(user_input):
    if user_input.find(' ') == -1:
        return user_input, ()
    else:
        t = tuple(user_input.split(' '))
        return t[0], t[1:]


def run():
    print('HTML Builder v0.1\n'
          'Type a command.Type help to see which commands are available.')

    while True:
        user_input = input("> ")
        if not user_input:
            continue

        command, args = interpret(user_input)
        if command == 'exit':
            break
        elif command == 'help':
            command.help.run(args)
        elif command == 'add':
            commands.add.run(args)
        elif command == 'files':
            commands.files.run(args)
        elif command == 'dir':
            commands.dir.run(args)
        elif command == 'load':
            commands.load.run(args)
