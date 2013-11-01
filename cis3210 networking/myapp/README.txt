Derek Dekroon
0709999
ddekroon@uoguelph.ca

Networking lab 6
\
To run this lab, run the paster server --reload development.ini on the command line then go to 127.0.0.1:5000

To use this lab, go to the Users Page (/users).
You'll probably need to create a user using the register option on the top navigation bar.
After you create a user you can log in using the log in form in the top navigation bar.
When you log in a cookie will be created on the browser then you'll be redirected to the login page.
You can go to /users, or /login and since you already have that cookie you'll automatically be directed to the successful login page.
To delete the cookie, select the logout option in the navigation bar of the login page.
The log out destroys the cookie, and from the log out page you can either log in or go to the users page.



Networking lab 5

To run this lab, run the paster server --reload development.ini on the command line then go to 127.0.0.1:5000

To use this lab, go to the Users Page. From there you can add a new user using the form at the bottom, delete a user using the delete individual users button, or delete all users. When you add a new user the username and password get escaped using the MySQLdb.escape_string() function. You must have something written in for both username AND password (strlen > 0) in order for the insert to work.

=======

Networking lab 4

This lab has two parts. The first is server testing. To run my tests paste this in the the terminal while inside the myapp folder:

nosetests -w myapp/tests/ test_myTest.py functional/test_mainController.py

This line does four total tests, two in tests/test_myTest.py, and two in tests/functional/test_mainController.py. The two in myTest.py are simple demos from the nosetest site that just make sure addition and subtraction are working. The two in the mainController test that Home is in the first index page, and User is in the users page. You should have 4 success in a fraction of a second.

The second part is client side testing. I created two selenium files, one seleniumIndex (selenium file for 127.0.0.1:5000), and one seleniumUsers (for 127.0.0.1:5000/users). They are both pretty standard, checks to see if the right body text shows up, correct title. The index file checks to see if myCookie doesn't exist. There is an option for does exist which I could see being very handy.
