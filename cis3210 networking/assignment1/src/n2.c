#include "nodeFunctions.h"

int main()
{
  int tmpFile1, tmpFile2;
  char msg[50];

  tmpFile1 = open("links/link1", O_RDONLY);
  read(tmpFile1, msg, 30);
  close(tmpFile1);
  printf("n2 Message %s Received\n", msg);

  mkfifo("links/link3", 0666);
  tmpFile2 = open("links/link3", O_WRONLY);
  write(tmpFile2, msg, sizeof(msg));
  close(tmpFile2);

  return 0;
}
