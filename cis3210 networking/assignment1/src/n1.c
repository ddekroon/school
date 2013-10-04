#include "nodeFunctions.h"

int main()
{
  char msg[30];
  char junkMsg[30];
  char * link1 = "links/link1", *link2 = "links/link2";
  //createLinks();

  while(strcmp(msg, "q\n") != 0) {
    fprintf(stdout, "Please enter your message (q to quit)\n");
    fgets(msg, 29, stdin);

    writeToLink(link1, msg);
    readFromLink(link1, junkMsg);
    writeToLink(link2, msg);
    readFromLink(link2, junkMsg);
  }
  //destroyLinks();
  return 0;
}
