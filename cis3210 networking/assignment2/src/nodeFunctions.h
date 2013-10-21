#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

void createLinks();
void destroyLinks();
void writeToLink(char * linkName, char * msg);
void readFromLink(char * linkName, char * returnMsg);
