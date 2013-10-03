#include "nodeFunctions.h"

void createLinks() {
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
  mkfifo("links/link1", 0666);
}
 
void writeToLink(char * linkName, char * msg) {
  int tmpFile;
  
  mkfifo(linkName, 0666);

  tmpFile = open(linkName, O_WRONLY);
  write(tmpFile, msg, sizeof(msg));
  close(tmpFile);
}

char * readFromLink(char * linkName) {
  int tmpFile;
  char * msg = calloc(30, sizeof(char));

  tmpFile = open(linkName, O_RDONLY);
  read(tmpFile, msg, 30);
  close(tmpFile);

  return msg;
}
