#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	long long n;
	scanf("%lld", &n);
	printf("%lld\n%d", (n * (n - 1) * (n - 2)) / 6, 3);
}