#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, pm = 2, chk = 0;
	scanf("%d", &n);
	while (n != 1) {
		if (n % pm == 0) {
			printf("%d\n", pm);
			n /= pm;
		}
		else
			pm++;
	}
}