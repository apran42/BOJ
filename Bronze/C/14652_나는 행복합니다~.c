#include <stdio.h>

int main() {
  int n, m, k;
  scanf("%d %d %d", &n, &m, &k);
  n=k/m;
  m=k%m;
  printf("%d %d", n, m);
  return 0;
}