Derek Dekroon
0709999
ddekroon@uoguelph.ca

Networking lab 5

To run this lab, run the paster server --reload development.ini on the command line then go to 127.0.0.1:5000

To use this lab, go to the Users Page. From there you can add a new user using the form at the bottom, delete a user using the delete individual users button, or delete all users. When you add a new user the username and password get escaped using the MySQLdb.escape_string() function. You must have something written in for both username AND password (strlen > 0) in order for the insert to work.
