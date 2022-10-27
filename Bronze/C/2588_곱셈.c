#include <stdio.h>

int main(void) {
  int a, b, c, d, e;
  scanf("%d", &a);
  scanf("%d", &b);
  e = b;
  c = b / 100;
  b %= 100;
  d = b / 10;
  b %= 10;
  
  printf("%d\n", a*b);
  printf("%d\n", a*d);
  printf("%d\n", a*c);
  printf("%d", a*e);
  
  return 0;
}