#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a1, a0, c, n0;
	scanf("%d %d", &a1, &a0);
	scanf("%d", &c);
	scanf("%d", &n0);

	if ((double)(a1 * n0 + a0) / (double)(c * n0) <= 1 && (c - a1 >= 0))
		puts("1");
	else
		puts("0");
}