/* Toggle GPIO pin 23 as fast as possible.
   GPIO 23 must be exported before this program runs.
   Once exported, file permissions for the gpio23 direction and value
   files must be set appropriately, if user is not root.

   Output pulse frequency is 120 kHz (typically varies a few kHz due to
   other activities such as network traffic, clock maintenence, etc.).
*/

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
  int       fd, fd2;

  fd = open("/sys/class/gpio/gpio23/value", O_RDWR);
  if (fd < 0)
    {
      perror("Open value failed");
      exit(2);
    }
  
  fd2 = open("/sys/class/gpio/gpio23/direction", O_RDWR);
  if (fd2 < 0)
    {
      perror("Open direction failed");
      exit(2);
    }
  else
    {
      if (3 != write(fd2, "out", 3))
	{
	  perror("Write direction failed");
	  exit(2);
	}
      close(fd2);
    }

  while (1)
    {
      if (0 > write(fd, "1", 1))
	{
	  perror("Write 1 failed");
	  exit(3);
	}
      if (0 > write(fd, "0", 1))
	{
	  perror("Write 0 failed");
	  exit(3);
	}
    }
  return 0;
}

