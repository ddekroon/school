CC=gcc
SRC='/src/'
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS= -c -Wall
COMMON_FILES = nodeFunctions.c nodeFunctions.h

all:	node1 node2 node3 node4 node5 node6 node7

node1:	$(SRC).n1.o
	$(CC) $(CFLAGS) n1.o -o n1
n1.o:	n1.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n1.c nodeFunctions.c

node2:	n2.o
	$(CC) $(CFLAGS) -o n2 n2.o
n2.o:	n2.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n2.c nodeFunctions.c

node3:	n3.o
	$(CC) $(CFLAGS) -o n3 n3.o
n3.o:	n3.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n3.c nodeFunctions.c

node4:	n4.o
	$(CC) $(CFLAGS) -o n4 n4.o
n4.o:	n4.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n4.c nodeFunctions.c

node5:	n5.o
	$(CC) $(CFLAGS) -o n5 n5.o
n5.o:	n5.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n5.c nodeFunctions.c

node6:	n6.o
	$(CC) $(CFLAGS) -o n6 n6.o
n6.o:	n6.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n6.c nodeFunctions.c

node7:	n7.o
	$(CC) $(CFLAGS) -o n7 n7.o
n7.o:	n7.c $(COMMON_FILES)
	$(CC) $(CFLAGS) -c n7.c nodeFunctions.c

clean:
	rm -rf *o hello
