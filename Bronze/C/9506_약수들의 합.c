#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	while (1) {
		int sum = 0;
		scanf("%d", &n);
		if (n == -1)
			break;
		for (int i = 1; i < n; i++) {
			if (n % i == 0)
				sum += i;
		}
		if (n != sum)
			printf("%d is NOT perfect.\n", n);
		else {
			sum = 0;
			printf("%d = ", n);
			for (int i = 1; i < n; i++) {
				if (n % i == 0) {
					sum += i;
					if (sum != n)
						printf("%d + ", i);
					else
						printf("%d\n", i);
				}
			}
		}
	}
}