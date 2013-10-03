CC=gcc
SRC=src/
BIN=bin/
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS= -Wall -g
LDFLAGS=
COMMON_FILES = src/nodeFunctions.c src/nodeFunctions.h

all:	node1 node2 node3 node4 node5 node6 node7

node1:	n1.o
	$(CC) $(CFLAGS) -o $(BIN)n1 n1.o
n1.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n1.c $(COMMON_FILES)

node2:	n2.o
	$(CC) $(CFLAGS) -o $(BIN)n2 n2.o
n2.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n2.c $(COMMON_FILES)

node3:	n3.o
	$(CC) $(CFLAGS) -o $(BIN)n3 n3.o
n3.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n3.c $(COMMON_FILES)

node4:	n4.o
	$(CC) $(CFLAGS) -o $(BIN)n4 n4.o
n4.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n4.c $(COMMON_FILES)

node5:	n5.o
	$(CC) $(CFLAGS) -o $(BIN)n5 n5.o
n5.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n5.c $(COMMON_FILES)

node6:	n6.o
	$(CC) $(CFLAGS) -o $(BIN)n6 n6.o
n6.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n6.c $(COMMON_FILES)

node7:	n7.o
	$(CC) $(CFLAGS) -o $(BIN)n7 n7.o
n7.o:	
	$(CC) $(LDFLAGS) -c $(SRC)n7.c $(COMMON_FILES)

clean:
	rm -rf *o bin/* links/*

run:
	bin/n1 & bin/n2 & bin/n3 & bin/n4 & bin/n5 & bin/n6 & bin/n7
