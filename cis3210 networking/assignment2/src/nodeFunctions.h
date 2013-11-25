#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>


/*Function used to send data through a link, it can send any message from one node to another */
void writeToLink(char * linkName, char * msg);

/*Reads from the link specified as linkName, gets put in to returnMsg */
void readFromLink(char * linkName, char * returnMsg);
