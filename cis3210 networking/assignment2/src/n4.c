#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link3";
  char msg[30];
  int strlen = 0;
  while(strcasecmp(msg, "quit") != 0) { 
    readFromLink(linkFile1, msg);
    
    if (msg[2] == '4') {
      if(strlen == 0) {
        printf("n4 receiving message:\n");
      }
    
      if(msg[0] != EOF) {
        printf("%c", msg[0]);
        strlen++;
      } else {
        strlen = 0;
      }
      writeToLink(linkFile1, "Received");
    }
  }
  writeToLink(linkFile1, "quit");
  return 0;
}
