#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, k, chk = 0;
	scanf("%d %d", &n, &k);
	for (int i = 1; i <= n; i++) {
		if (n % i == 0)
			chk++;
		if (n % i == 0 && chk == k) {
			printf("%d", i);
			break;
		}
	}
	if (chk < k)
		printf("0");
}