Derek Dekroon
0709999
ddekroon@uoguelph.ca

Networking lab 4

This lab has two parts. The first is server testing. To run my tests paste this in the the terminal while inside the myapp folder:

nosetests -w myapp/tests/ test_myTest.py functional/test_mainController.py

This line does four total tests, two in tests/test_myTest.py, and two in tests/functional/test_mainController.py. The two in myTest.py are simple demos from the nosetest site that just make sure addition and subtraction are working. The two in the mainController test that Home is in the first index page, and User is in the users page. You should have 4 success in a fraction of a second.

The second part is client side testing. I created two selenium files, one seleniumIndex (selenium file for 127.0.0.1:5000), and one seleniumUsers (for 127.0.0.1:5000/users). They are both pretty standard, checks to see if the right body text shows up, correct title. The index file checks to see if myCookie doesn't exist. There is an option for does exist which I could see being very handy.
