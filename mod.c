#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){

  int val1, val2, modval;

  if (argc != 3) {
      printf("Usage: wrong\n");
      exit(1);
  }
  val1= atoi(argv[1]);
  val2= atoi(argv[2]);
  modval = val1 % val2;

  printf ("v1(%d) v2(%d) v1 MOD v2 = %2d\n", val1, val2, modval);

  exit(0);
  
}
