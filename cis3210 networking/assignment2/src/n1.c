#include "nodeFunctions.h"

int main()
{
  char msg[30], junkMsg[200];
  char * link1 = "links/link1", *link2 = "links/link2", *sendLink;
  char * fileName, * node;
  FILE * fileptr;
  int nodeNum, errorCheck = 0;
  char fileChar;

  while(strcasecmp(msg, "n\n") != 0) {
    errorCheck = 0;
    fprintf(stdout, "Please enter the file name and what node to connect to\n");
    fgets(msg, 29, stdin);

    fileName = strtok(msg, " ");
    node = strtok(NULL, " ");

    nodeNum = (int)node[1] - 48;

    if(node[0] != 'n' || nodeNum > 7 || nodeNum < 2) {
      fprintf(stdout, "Error, node given does not exist. Use format n#\n");
      errorCheck = 1;
    }
    
    if((fileptr = fopen(fileName, "r")) == NULL) {
      perror("Error opening file");
      errorCheck = 1;
    }
   
    if(errorCheck == 0) {
      if(nodeNum == 2 || nodeNum == 4) {
        sendLink = link1;
      } else {
        sendLink = link2;
      }
    
      writeToLink(sendLink, "Sending\0");
      while(!feof(fileptr)) {
        fileChar = fgetc(fileptr);
        msg[0] = fileChar;
        msg[1] = 'n';
        msg[2] = node[1];
        msg[3] = '\0';
        writeToLink(sendLink, msg);
        readFromLink(sendLink, junkMsg);
      }
      fclose(fileptr);
    }

    fprintf(stdout, "Would you like to continue? (Y/N)\n");
    fgets(msg, 29, stdin);
  }
  writeToLink(link1, "quit");
  readFromLink(link1, junkMsg);
  writeToLink(link2, "quit");
  readFromLink(link2, junkMsg);

  return 0;
}
