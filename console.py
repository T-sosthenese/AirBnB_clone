#!/usr/bin/python3
"""
Command line interpreter/console for hbnb
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ The prompt for our HBNB console/command line interpreter."""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits the program when the end of file is reached."""
        quit()
        return True

    def do_quit(self, arg):
        """ Quit command that exits the current program."""
        quit()
        return True

    def emptyline(self):
        """Prints and empty line to prompt the user for input."""
        return False

    def do_help(self, args):
        """Lists all the functionalities available for a particular help."""
        cmd.Cmd.do_help(self, args)
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
