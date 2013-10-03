#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

void createLinks();
void writeToLink(char * linkName, char * msg);
char * readFromLink(char * linkName);
