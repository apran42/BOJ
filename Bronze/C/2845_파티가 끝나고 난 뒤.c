#include <stdio.h>
int main() {
  int n,p;
  long a,b,c,d,e;
  scanf("%d %d", &n, &p);
  scanf("%ld %ld %ld %ld %ld", &a,&b,&c,&d,&e);
  printf("%ld %ld %ld %ld %ld", a-(n*p), b-(n*p), c-(n*p), d-(n*p), e-(n*p));
}