#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link6";
  char msg[30];

  while(strcmp(msg, "q\n") != 0) {
    readFromLink(linkFile1, msg);
    printf("n7 Message %s Received\n", msg);

    writeToLink(linkFile1, msg);
  }

  return 0;
}
