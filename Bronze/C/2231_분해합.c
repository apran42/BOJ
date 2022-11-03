#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	int chk = 0;
	scanf("%d", &n);
	for (int i = 1; i < n; i++) {
		int sum = 0;
		int num = i;
		sum += num;
		
		while (num != 0) {
			sum += num % 10;
			num /= 10;
		}
		
		if (sum == n) {
			printf("%d", i);
			chk = 1;
			break;
		}
	}
	if (chk != 1)
		printf("%d", 0);
	return 0;
}