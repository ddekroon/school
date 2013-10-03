#include "nodeFunctions.h"
#include <string.h>

int main(args) {
  char msg[30]; 
  char * link1 = "links/link1";
  char * link2="links/link2";
  int tmpFile1, tmpFile2;

    fprintf(stdout, "Please enter the command to send to other nodes\n");
    fgets(msg, 30, stdin);

    fprintf(stderr, "message - %s\n", msg);
    mkfifo(link1, 0666);
    
    fprintf(stdout, "Made fifo");
    tmpFile1 = open(link1, O_WRONLY);
    
    fprintf(stderr, "past creating link");
    
    write(tmpFile1, msg, sizeof(msg));
    close(tmpFile1);

    fprintf(stderr, "okay");

    mkfifo(link2, 0666);
    tmpFile2 = open(link2, O_WRONLY);
    write(tmpFile2, msg, sizeof(msg));
    close(tmpFile2);
 
  return 0;
}
