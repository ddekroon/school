#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link3";
  char msg[30];

  while(strcmp(msg, "q\n") != 0) {
    readFromLink(linkFile1, msg);
    printf("n4 Message %s Received\n", msg);

    writeToLink(linkFile1, "Message Received");
  }
  fprintf(stderr, "n4 exiting\n");
  return 0;
}
