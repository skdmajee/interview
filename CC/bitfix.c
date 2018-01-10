#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

/*
 * Extract  k bits from position p of number n
 * Reference: https://www.geeksforgeeks.org/python-slicing-extract-k-bits-given-position/
 *
 */
int extract_bits(int n, int pos, int k)
{
  int mask;

  mask = (1<<k)-1;
  return ((n>>(pos-1)) & mask);
}

char *printb(int n)
{
  static char c[256];
  char *p, *s;
  int i, len;

  // find the len
  i=n;
  len=0;
  while (i) {
    len++;
    i=i>>1;
  }
  //printf("len=%d\n",len);

  c[len]=0;
  p=&c[len-1];
  while (n){
    *p= (n&0x1)?'1':'0';
    //printf("%d:: %c ",n, *p);
    p--; 
    n= n>>1;
  }
  s = malloc(len+1);
  if (s==NULL){
    printf("ERROR: malloc failed\n");
    return (NULL);
  }
  strcpy(s,c);
  //printf("RET=%s\n", s);
  return s;
}

void usage(char *prog)
{
  printf("Usage:%s number\n", prog);
  exit(1);
}


int main(int argc, char *argv[])
{

  int x,y, n,i,p,k;

  if (argc < 2)
    usage(argv[0]);

  n=atoi(argv[1]);

  n=28;
  x = (n>>3) & ((1U<<2)-1);
  x = ((1U<<3) - 1);
  x = ((1U<<3));
  printf("28 shift etc(%s)\n", printb(x));

  n=171;
  printf("========================\n");
  printf ("Given number= %d: %s\n",n, printb(n));
  x = extract_bits(n, 2, 5);
  printf("1. Extract 5 bits from pos 2: %d :: %s\n",x, printb(x));




}
