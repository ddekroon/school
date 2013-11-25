Derek Dekroon
0709999
ddekroon@uoguelph.ca

Assignment2

To run this program, type make, then make run.

This program asks the user for a name of a file, and the number for which node to send the contents of the file to.

It uses the same scheme as assignment1, so to get to nodes 5-7 you need to go through n3, and n4 goes through n2.

It gets the name of the file, checks if it exists, then goes through the characters 1 by 1. Every time it gets a char it sends that char, and the node to send to through the link. The receiving node gets the data, figures out what node it should (if any) send the data to, then waits for a response. All links are closed as soon as the data is received, then reopened where appropriate. The structure will only use read only and write only to convey the message.

To exit the program, simply say you don't want to continue when prompted.

I had an issue where the program infinite loops on startup... but it only happened on one computer so I really hope it doesn't happen to you. Otherwise I believe all the programs should function normally.
