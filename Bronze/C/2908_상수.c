#include <stdio.h>
int main(void) {
	int a, b = 0;
	scanf("%d %d", &a, &b);
	a = (a % 10 * 100) + (a / 10 % 10 * 10) + (a / 100);
	b = (b % 10 * 100) + (b / 10 % 10 * 10) + (b / 100);
	if (a > b) printf("%d", a);
	else printf("%d", b);
	return 0;
}