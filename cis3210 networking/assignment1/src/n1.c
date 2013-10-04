#include "nodeFunctions.h"

int main()
{
  char msg[30];
  char * link1 = "links/link1", *link2 = "links/link2";
  int readInt, writeInt; 
  createLinks();

  while(strcmp(msg, "q\n") != 0) {
    fprintf(stdout, "Please enter your message (q to quit)\n");
    fgets(msg, 30, stdin);

    writeToLink(link1, msg);
    readFromLink(link1, msg);
    writeToLink(link2, msg);
    readFromLink(link2, msg);
  }
  destroyLinks();
  return 0;
}
