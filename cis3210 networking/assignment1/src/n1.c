#include "nodeFunctions.h"
#include <string.h>


int main()
{
  char msg[50];
  char * link1 = "links/link1", *link2 = "links/link2";

  while(strcmp(msg, "q\n") != 0) {
    fprintf(stdout, "Please enter your message (q to quit)\n");
    fgets(msg, 30, stdin);

    writeToLink(link1, msg);
    writeToLink(link2, msg);
    
  }

  return 0;
}
