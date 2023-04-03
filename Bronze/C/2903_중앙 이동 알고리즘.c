#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {
	int a = 2, n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		a = a + (int)pow(2, (i - 1));
	}
		printf("%d", a * a);
}