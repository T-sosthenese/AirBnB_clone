#!/usr/bin/python3
"""
Command line interpreter/console for hbnb
"""


import cmd
import shlex
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State

classes = {"BaseModel": BaseModel, "User": User, "City": City, "Place": Place,
           "Amenity": Amenity, "Review": Review, "State": State}


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

    def do_create(self, arg):
        """Creates a new instance for the specified class."""
        args = shlex.split(arg)  # Splits cmdline args separated by spaces
        if len(args) == 0:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name in classes:
            instance = classes[class_name]()  # Accessing classes dict value
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints the string representation of all classes."""
        args = shlex.split(arg)
        all_objects = []
        if len(args) == 0:
            for value in storage.all().values():
                all_objects.append(str(value))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        elif args[0] in classes:
            for key in storage.all():
                if args[0] in key:
                    all_objects.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(all_objects), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates class attributes based on provided instances."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                immutable_attrs = ["id", "created_at", "updated_at"]
                if obj:
                    tokens = shlex.split(arg)
                    if len(tokens) < 3:
                        print("** attribute name missing **")
                    elif len(tokens) < 4:
                        print("** value missing **")
                    elif tokens[2] not in immutable_attrs:
                        obj.__dict__[tokens[2]] = tokens[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
