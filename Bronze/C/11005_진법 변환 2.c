#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

int main() {
	int n, b, chk = 0;
	char res[32] = { "", };
	scanf("%d %d", &n, &b);
	int digit = 31;
	for (int i = 0; i < 32; i++) {
		int tmp = n / (int)pow(b, digit);
		if (tmp < 10)
			res[i] = tmp + 48;
		if (tmp >= 10 && tmp < 36)
			res[i] = tmp + 55;
		n -= (tmp * (int)pow(b, digit));
		digit--;
	}
	for (int i = 0; i < 32; i++) {
		if (res[i] == '0' && chk == -1)
			printf("%c", res[i]);
		if (res[i] != '0') {
			chk = -1;
			printf("%c", res[i]);
		}
	}
}