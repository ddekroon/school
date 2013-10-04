#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link1", *linkFile2 = "links/link3";
  char msg[30];
  while(strcmp(msg, "q\n") != 0) {
    readFromLink(linkFile1, msg);
    printf("n2 Message %s Received\n", msg);

    writeToLink(linkFile2, msg);
    readFromLink(linkFile2, msg);
    writeToLink(linkFile1, msg);
  }
  return 0;
}
