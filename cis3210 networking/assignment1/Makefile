CC=gcc
SRC=src/
BIN=bin/
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS= -Wall -g
LDFLAGS=
COMMON_FILES = src/nodeFunctions.c src/nodeFunctions.h

all:	node1 node2 node3 node4 node5 node6 node7

node1:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n1.c -o $(BIN)n1

node2:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n2.c -o $(BIN)n2

node3:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n3.c -o $(BIN)n3

node4:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n4.c -o $(BIN)n4

node5:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n5.c -o $(BIN)n5

node6:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n6.c -o $(BIN)n6

node7:	nodeFunctions.o
	$(CC) $(CFLAGS) nodeFunctions.o $(SRC)n7.c -o $(BIN)n7

nodeFunctions.o:
	$(CC) $(LDFLAGS) -c $(COMMON_FILES)


clean:
	rm -rf *o bin/* links/*

run:
	bin/n5 & bin/n4 & bin/n3 & bin/n2 & bin/n1
