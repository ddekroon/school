#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link2", *linkFile2 = "links/link4", *linkFile3 = "links/link5", *linkFile4 = "links/link6";
  char msg[30];
  
  while(strcmp(msg, "q\n") != 0) {
    readFromLink(linkFile1, msg);
    printf("n3 Message %s Received\n", msg);
    
    writeToLink(linkFile2, msg);
    readFromLink(linkFile2, msg);
    writeToLink(linkFile1, msg);
    
    //writeToLink(linkFile3, msg);
    //writeToLink(linkFile4, msg);

  }
  return 0;
}
