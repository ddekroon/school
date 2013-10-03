#include "nodeFunctions.h"

int main()
{
  char * linkFile1 = "links/link1", *linkFile2 = "links/link3";
  char * msg;

  msg = readFromLink(linkFile1);
  printf("n2 Message %s Received\n", msg);

  writeToLink(linkFile2, msg);
  free(msg);
  return 0;
}
