#include "nodeFunctions.h"

void writeToLink(char * linkName, char * msg) {
  int tmpFile;
  char sendMsg[30];
  strcpy(sendMsg, msg);
  sendMsg[30] = '\0';
  if( access( linkName, F_OK ) == -1 ) {
    fprintf(stderr, "Link %s created by write funtion\n", linkName);
    mkfifo(linkName, 0777);
  }

  if((tmpFile = open(linkName, O_WRONLY)) < 0) {
    fprintf(stderr, "error opening stream to write - %s, %s", linkName, strerror(errno));
  } else {
    if(write(tmpFile, sendMsg, 30) < 0) {
      fprintf(stderr, "error writing to %s, %s", linkName, strerror(errno));
    }
    close(tmpFile);
  }
}

void readFromLink(char * linkName, char * returnMsg) {
  int tmpFile;
  char msg[30];
  if(access(linkName, F_OK) == -1) {
    mkfifo(linkName, 0777);
  }
  if((tmpFile = open(linkName, O_RDONLY)) < 0) {
    fprintf(stderr, "error opening stream to read - %s, %s", linkName, strerror(errno));
    strcpy(msg, "read error");
  } else {
    if(read(tmpFile, msg, 30) < 0) {
      fprintf(stderr, "error reading from %s, %s\n", linkName, strerror(errno));
    }
    close(tmpFile);
  }
  strcpy(returnMsg, msg);
}
