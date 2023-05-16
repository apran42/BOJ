#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int cnt = 0;
	int sixs = 666;
	while (n != cnt) {
		int tmp = sixs;
		while (tmp != 0) {
			if (tmp % 1000 == 666) {
				cnt++;
				break;
			}
			tmp /= 10;
		}
		sixs++;
	}
	printf("%d", sixs-1);
}