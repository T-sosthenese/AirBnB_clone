### AirBnB Clone - The Console
-----
#### Description
AirBnB is a complete web application, integrating database storage, a backend API, and front-end interface. This is the first part of the project which primarily focuses on making the commandline interpreter (console) that will be used to run simple commands on the project.
Here are a few operations of the console:
* ./console.py - the command used to launch/run the console
* help - displays all the available commands on the console
* quit - the command used to quit the console
* create classname - command used to create an instance of an object
* all classname - the command used to display all objects stored in the engine's file storage
* show classname id - command used to show a specific class instance
* destroy classname id - deletes an instance based on its classname and id
* all - prints the string representation of all instances
* update classname id attribute-name attribute-value - updates an instance
* classname.all() - displays all the instances of the specified class.
* classname.count() - prints the instances of a class in file storage
* classname.show(id) - retrieves the instance of a class using its id.
* classname.destroy(id) - destroys class instance based on the id
* classname.update(id), attributename, attributevalue - updates instance values
* classname.update(id, dictionary-representation) - updating instance based on its dict id
