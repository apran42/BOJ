#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int n1 = n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			printf(" ");
		}

		for (int k = 0; k < n - i; k++) {
			printf("*");
		}
		puts("");
	}
	return 0;
}