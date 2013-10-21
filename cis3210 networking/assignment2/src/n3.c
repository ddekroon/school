#include "nodeFunctions.h"

int main() {
  char * linkFile1 = "links/link2", *linkFile2 = "links/link4", *linkFile3 = "links/link5", *linkFile4 = "links/link6";
  char msg[30];
  char junkMsg[30];
  int strlen = 0;

  while(strcasecmp(msg, "quit") != 0) {
    readFromLink(linkFile1, msg);

    if(msg[2] == '5') {
      writeToLink(linkFile2, msg);
      readFromLink(linkFile2, junkMsg);
      writeToLink(linkFile1, "Received");
    } else if(msg[2] == '6') {
      writeToLink(linkFile3, msg);
      readFromLink(linkFile3, junkMsg);
      writeToLink(linkFile1, "Received");
    } else if(msg[2] == '7') {
      writeToLink(linkFile4, msg);
      readFromLink(linkFile4, junkMsg);
      writeToLink(linkFile1, "Received");
    } else if (msg[2] == '3') {
      if(strlen == 0) {
        printf("n3 receiving message:\n");
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
  
  writeToLink(linkFile2, "quit");
  readFromLink(linkFile2, junkMsg);
  writeToLink(linkFile3, "quit");
  readFromLink(linkFile3, junkMsg);
  writeToLink(linkFile4, "quit");
  readFromLink(linkFile4, junkMsg);
  writeToLink(linkFile1, "Message Reeived");
  return 0;
}
