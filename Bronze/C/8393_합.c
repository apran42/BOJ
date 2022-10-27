#include <stdio.h>
int main(void) {
	int n = 0;
	scanf("%d", &n);
	n = n * (n + 1) / 2;
	printf("%d", n);
	return 0;
}