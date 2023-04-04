#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, b;
	while (1) {
		scanf("%d %d", &a, &b);
		if (a == 0 && b == 0)
			break;
		if (b % a == 0)
			puts("factor");
		else if (a % b == 0)
			puts("multiple");
		else
			puts("neither");
	}
}