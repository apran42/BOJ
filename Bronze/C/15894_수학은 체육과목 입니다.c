#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	unsigned res = 0;
	scanf("%d", &n);
	res = 4 * (unsigned int)n;
	printf("%u", res);
}